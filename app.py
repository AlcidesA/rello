from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost/rello'

db = SQLAlchemy(app)

@app.route('/user', methods=['POST'])
def create_user():
    name = request.json['name']
    email = request.json['email']
    
    new_user = User(name, email)
    
    db.session.add(new_user)
    db.session.commit()
    
    return {
        'name': new_user.name,
        'email': new_user.email
    }


class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(50))

    def __init__(self, name, email):
        self.name = name
        self.email = email