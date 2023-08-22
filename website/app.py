from module.__init__ import *

app = Flask(import_name=__name__)
app.config['SECRET_KEY'] = 'secret!'
app.debug = False
socketio = SocketIO(app,debug=not app.debug)

