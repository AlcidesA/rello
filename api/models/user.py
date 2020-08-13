from app import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), nullable = False)
    email = db.Column(db.String(50), nullable = False, unique = True)
    password = db.Column(db.String(128), nullable = False)

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password =  generate_password_hash(password)

    def add(new_user):
        db.session.add(new_user)
        db.session.commit()

        return {
            'name': new_user.name,
            'email': new_user.email
        }
    
    def authenticate(self, password):
        return check_password_hash(self.password, password)