from app import app
from flask import request
from api import api
from api.models.user import User
from datetime import datetime, timedelta
from jwt import encode

@api.route('/register', methods=['POST'])
def register():
    name = request.json['name']
    email = request.json['email']
    password = request.json['password']
    
    new_user = User(name, email, password).add()
    
    return new_user

@api.route('/login', methods=['POST'])
def login():
    email = request.json['email']
    password = request.json['password']

    user = User.query.filter_by(email = email).first_or_404()

    if not user.authenticate(password):
        return {
            'error': 'Invalid credentials!'
        }, 403

    payload = {
        'id': user.id,
        'exp': datetime.utcnow() + timedelta(minutes = 10)
    }

    token = encode(payload, app.config['SECRET_KEY'])

    return {"token": token.decode('utf-8')}