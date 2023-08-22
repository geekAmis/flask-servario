import os, pip
pip.main(['install', 'tqdm'])
import tqdm

class Load_Libs(object):
	"""docstring for Load_Libs
		Все modules должны быть правильными по названию, иначе всё... Жопа.
		Короче, используйте правильные названия всех библиотек

		Пример:
		modules = [
			"import name",
			"from name import allalalal",
			"import gigachad"
		]
	"""
	def __init__(self,modules, FileName='__init__',token='',tg_id=0,endles_word="All Libs be install\\n\\nBy XGEMX Lilanga - FRG Team"):
		super(Load_Libs, self).__init__()
		self.moduleFileName = f'module/{FileName}.py'
		self.modules = modules
		self.token = token
		self.tg_id = tg_id
		self.nt = os.name
		self.modulesSplitter = self._modules_split()
		self.endles_word = endles_word
		if not os.path.exists(self.moduleFileName):  
			self.moduleFileType()


	"""modules_split служит для получения имён библиотек, которые импортируются в проект"""
	def _modules_split(self):
		return [module.split(' ')[1] if module != '' else 'requests' for module in [self.modules.pop(self.modules.index(i)) if i == '' else i for i in self.modules]]


	def moduleFileType(self):
		with open(self.moduleFileName,'w',encoding='UTF-8') as self.file_write:
			self.InstallAll()

	def InstallAll(self):
		for self.module in tqdm.tqdm(self.modulesSplitter):
			try:
				os.system(str('pip' if self.nt == 'nt' else 'pip3')+f' install {self.module}')
			except Exception as error:
				os.system(f'echo {error}')
			self.file_write.write(self.modules[self.modulesSplitter.index(self.module)]+'\n');os.system('cls')
			# да, я знаю, что это не оптимальное решение лучше сразу через иттер, но так читабельность выше

		self.file_write.write(f'print("{self.endles_word}")\nTELEGRAM_TOKEN = "{self.token}"\nTELEGRAM_ID = int({self.tg_id})')
		return True
		
