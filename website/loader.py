from website.app import *

_POOL = []

class Website: # Сделан для избегания ошибок стандартного flask.
	def __init__(self,template) -> None:
		self.template = template
		self.render_template()

	def render_template(self):
		with open(f'website/html/{self.template}','r',encoding='UTF-8') as self.template_render:
			self.template_render = self.template_render.read();return self.template_render

	def set_args(self,**args):
		for key, value in args.items():
			self.template_render = self.template_render.replace('{{'+key+'}}',value)
		return self.template_render

"""

		LOAD FILES IN PATH

"""

@app.route('/assets/<path:path>/<filename>')
def assets(path,filename):
	return send_from_directory(f'{path}', filename)

@app.route('/<filename>')
def render_file_in(filename):
	return Website(filename).render_template()


"""

	RENDER TEMPLATES

"""


@app.route('/',methods=['GET','POST'])
def index_template():
	if request.method == 'POST':
		if "m" not in str(request.form.get("email")):
			return Website('403.html').set_args(Markup('Простите, но такую почту я не знаю, воспользуйтесь telegram или напишите на мою почту самолично: <a href="mailto:xgemxsite@gmail.com">xgemxsite@gmail.com</a>'))
		requests.get("https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}&parse_mode=HTML".format(
			TELEGRAM_TOKEN,TELEGRAM_ID,f"""<i>{request.form.get("name")}</i>
			<code>{request.form.get("message")}</code>

			<a href="mailto://{request.form.get("email")}">{request.form.get("email")}</a>
			<tg-spoiler>IP: {request.form.get("ip")}</tg-spoiler>
			"""
		))
	return Website('index.html').set_args(company_name='Lilanga портфолио')


"""

	SECOND FUNCTIONS

"""


@app.route('/pool',methods=['POST'])
def pool_loader():
	if request.form.get("item_index"):
		return jsonify({"item": _POOL[int(request.form.get("item_index"))]})
	elif request.form.get("load_code"):
		_POOL.append(Markup(str(request.form.get("load_code"))))
		return jsonify({"status_code":200,"item_index":_POOL.index(_POOL[-1])})


@app.route('/ip')
def get_user_ip():
	return str(request.headers.get('X-Real-IP'))


"""
		ERROR PAGES TEMPLATES

"""
@app.errorhandler(404)
def page_not_found(e):
	# note that we set the 404 status explicitly
	return Website('404.html').render_template(), 404

@app.errorhandler(403)
def page_access_denied(e):
	# note that we set the 404 status explicitly
	return Website('403.html').set_args(msg=Markup('Не пущу <span>тебя</span> дальше.')), 403


