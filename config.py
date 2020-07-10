import os
import base64
from configparser import ConfigParser 

configur = ConfigParser()
configur.read('config.ini')

class Config(object):
    URL = configur.get('NPROD', 'URL')
    PWD = base64.b64decode(configur.get('NPROD', 'PWD')).decode('utf-8')
    USER = base64.b64decode(configur.get('NPROD', 'User')).decode('utf-8')

