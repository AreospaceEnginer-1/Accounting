from flask_wtf import Form
from wtforms import TextField, IntegerField, TextAreaField, SubmitField, RadioField, SelectField
from wtforms import validators, ValidationError
import Account

class Account(Form):
   name = TextField("Name Of Student",[validators.Required("Please enter your name.")])
   Gender = RadioField('Gender', choices = [('M','Male'),('F','Female')])
   Address = TextAreaField("Address")
   email = TextField("Email",[validators.Required("Please enter your email address."), \
   validators.Email("Please enter your email address.")])
   Age = IntegerField("Age")
   submit = SubmitField("Send")

   def upload():
       pass
 
