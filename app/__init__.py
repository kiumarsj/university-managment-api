from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# from flask_script import Manager
from flask_login import LoginManager
from flask_mail import Mail
from config import *

app = Flask(__name__)
# app.config.from_object('config.Config')
app.config.from_object(DevelopmentConfig)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
# manager = Manager(app)
login_manager = LoginManager(app)
mail = Mail(app)

from app.views import *

@app.route('/')
def index():
    return jsonify({'message': 'Welcome to the University Management System API.'})
