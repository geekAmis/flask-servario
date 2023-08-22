import json
class Config:
	"""docstring for Config"""
	def __init__(self):
		super(Config, self).__init__()
		self.load_config()
	
	def load_config(self):
		with open('config.json','r',encoding='UTF-8') as self.jsonFile:  self.jsonFile = json.load(self.jsonFile)

	def get(self,key):  return self.jsonFile.get(key)
	
	def getWebAddress(self):  
		if self.jsonFile.get("port"):
			return str( 'https://' if self.jsonFile.get("port") == 443 else 'http://' )\
			 + self.jsonFile.get("host")\
			 + str( f':{self.jsonFile.get("port")}' if self.jsonFile.get("port") not in [80,443] else '' )