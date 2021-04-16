from os import getenv, path
from dotenv import load_dotenv

APP_ROOT = path.join(path.dirname(__file__), '.')   # refers to application_top
dotenv_path = path.join(APP_ROOT, '.env')
load_dotenv(dotenv_path)


class Config(object):

    DEPLOY_ENV = getenv('RUN_ENV','dev')

    SERVER_PORT = getenv('SERVER_PORT','9000')
    
    MONGODB_SETTINGS = {
        'host' : getenv('MONGODB_URI')
    }



