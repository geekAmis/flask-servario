import os
import os
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
import os
print("All Libs be install\n\nBy XGEMX Lilanga - FRG Team")
TELEGRAM_TOKEN = "5955811135:AAGu7qDTCcz-ChbupcI-_CLiKxq2xjEj2OI"
TELEGRAM_ID = int(5091972921)