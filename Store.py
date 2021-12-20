from .main import db
from flask_login import UserMixin

class Jinja2_NOT_ReadableError(Exception): pass

class Accounts(db.Model, UserMixin):
    Id = db.Column(db.Integer, primary_key = True) 
    Name = db.Column(db.String(50), nullable = False) 
    Email = db.Column(db.String(50), nullable = False, unique = True)
    Address = db.Column(db.String(1000), nullable = False)
    Pincode = db.Column(db.Integer, nullable = False)
    DOB = db.Column(db.DateTime, nullable = False)
    Password = db.Column(db.String(10), nullable = False)
    U_name = db.Column(db.String(30), nullable = False, unique = True)