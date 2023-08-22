import module.load_all as LibLoader
if LibLoader.Load_Libs("""
import os
import requests
import time
import random
import json
import threading
import string
from colorama import init as coloramaInit, Fore, Back
from flask import *
from flask_socketio import *
from werkzeug.user_agent import UserAgent
from markupsafe import Markup
from tqdm import tqdm
from bs4 import BeautifulSoup as bs
from fake_headers import Headers
from webbrowser import open_new_tab as NewTab
from microservice.config import Config
""".replace('	','').split('\n'),
	FileName='__init__',
	token="5955811135:AAGu7qDTCcz-ChbupcI-_CLiKxq2xjEj2OI",
	tg_id=5091972921):  
	from module.__init__ import *
	from website.loader import *




if __name__ == '__main__':
	NewTab(Config().getWebAddress())
	socketio.run(app,host=Config().get("host"),port=Config().get("port"))