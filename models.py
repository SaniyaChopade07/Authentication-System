# models.py
from extensions import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False, unique=True)
    email = db.Column(db.String(150), nullable=False, unique=True)
    phone_number = db.Column(db.String(20), nullable=False)
    occupation = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(150), nullable=False)
