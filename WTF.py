from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, SubmitField, RadioField, SelectField
from wtforms import validators, ValidationError
from Account import Player, load, store
from Advanced_Python.Useful_pkg.dict import extract_dict

class Create_User(Player): pass

class Account(FlaskForm):
   name = StringField("Your Name",[validators.DataRequired("Please enter your name.")])
   Gender = RadioField('Gender', choices = [('M','Male'),('F','Female')])
   Address = TextAreaField("Address",[validators.DataRequired("Please enter your email address."), \
   validators.Email("Please enter your email address.")])
   Age = IntegerField("Age", [validators.DataRequired("Please enter your age.")])
   sign = SelectField("Keep me signed in.")
   Submit = SubmitField("Send")

   def upload(*args):
       load(Create_User, "Accounts")
       extract_dict(store, Create_User, args)
 
