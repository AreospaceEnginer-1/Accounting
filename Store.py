from flask_sqlalcemy import SQLAlchemy
from Accounet import web_page

db = SQLAlchemy(web_page) 

class Accounts(db.Model):
    Id = db.Column(db.Integer, primary_key = True) 
    Name = db.Column(db.String(50), nullable = False) 
    Email = db.Column(db.String(50), nullable = False)
    Address = db.Column(db.String(1000), nullable = False)
    Pincode = db.Column(db.Integer, nullable = False)
    DOB = db.Column(db.DateTime, nullable = False)
    Password = db.Column(db.String(10), nullable = False)
    U_name = db.Column(db.String(30), nullable = False)
