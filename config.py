#Eigenentwicklung
import os
from dotenv import load_dotenv
basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


#Eigenentwicklung. Der Secret-Key, die Datenbank-URL sowie Benutzername und Passwort sind in der .env-Datei abgelegt.
class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'Y3/a=-pN33ne8.g8'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
