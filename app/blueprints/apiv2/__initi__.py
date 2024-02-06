from flask import Blueprint, request

blueprintv2 = Blueprint('api', __name__, url_prefix='/api/v2')

@blueprintv2.route('/hello_world')
def hello_world():
    return {'message': 'Hello World!'}
