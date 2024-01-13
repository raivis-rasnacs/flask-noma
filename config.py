from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

class Config:

    STATIC_FOLDER = 'static'
    STATIC_URL_PATH = '/static'
    
    FLASK_ENVIRONMENT = environ['FLASK_ENVIRONMENT']
    SQLALCHEMY_DATABASE_URI = environ['DATABASE_URL']
    SQLALCHEMY_TRACK_MODIFICATIONS = False