from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config.from_object('config.Development')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://user_test:Luis9485326*@127.0.0.1/test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
bcrypt = Bcrypt(app)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app.routes import *

# @app.route('/')
# def index():
#    return "Hola"

