import os
import base64
from configparser import ConfigParser 
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

configur = ConfigParser()
configur.read('config.ini')


class Config(object):
    environment = os.environ.get('ZBX_ENV') or 'NPROD'
    URL = configur.get(environment, 'URL')
    PWD = base64.b64decode(configur.get(environment, 'PWD')).decode('utf-8')
    USER = base64.b64decode(configur.get(environment, 'User')).decode('utf-8')
    ACTION = configur.get(environment, 'ACTION')

