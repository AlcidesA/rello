from flask import request
from api import api
from api.models.user import User

@api.route('/user', methods=['POST'])
def create_user():
    name = request.json['name']
    email = request.json['email']
    
    new_user = User(name, email).add()
    
    return new_user