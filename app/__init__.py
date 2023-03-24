from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# from flask_login import LoginManager
from flask_mail import Mail
from app.blueprints.apiv1 import blueprint as bluev1
# from app.blueprints.apiv2 import blueprint as bluev2
from config import *

app = Flask(__name__)
app.register_blueprint(bluev1)
# app.register_blueprint(bluev2)
# app.config.from_object('config.Config')
app.config.from_object(DevelopmentConfig)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
# login_manager = LoginManager(app)
mail = Mail(app)
from app.views import *

@app.route('/')
def index():
    if request.headers.get("Content-Type") in ['application/json', 'Application/JSON'] or request.headers.get("content-type") in ['application/json', 'Application/JSON']:
        return jsonify({'message': 'Welcome to the University Management System API.'}), 200
    else:
        return render_template('index.html'), 200
