from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mail import Mail

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)
migrate = Migrate(app, db)
mail = Mail(app)

from app.views import *

@app.route('/')
def index():
    return jsonify({'message': 'Welcome to the University Management System API.'})
