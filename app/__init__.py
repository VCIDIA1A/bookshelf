#Übernommen
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bootstrap import Bootstrap

#Eigenentwicklung
app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'
login.login_message = "Bitte melde dich mit deinem bookshelf-Konto an."
bootstrap = Bootstrap(app)

#Übernommen
from app import routes, models, errors, api
