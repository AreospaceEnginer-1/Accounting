from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class Register(FlaskForm):
   name = StringField("Your Name", validators = [DataRequired("Please give a username")])
   username = StringField("Username", validators = [DataRequired("Please give a username")])
   # email = StringField("Email", validators=[DataRequired("Please give a email"),
   #    Email("Enter a valid email")])
   # age = IntegerField("Age", validators=[DataRequired("Please give a age")])
   # password = PasswordField("Password", validators = [DataRequired("Please give a password"),
   #     EqualTo('c_password', message="Your password is not equal to your confirm password")])
   # c_password = PasswordField("Confirm Password", validators = [DataRequired("Please confirm your password")])
   submit = SubmitField("Register")

class Login(FlaskForm):
   username = StringField("Username", validators = [DataRequired()])
   password = PasswordField("Password", validators = [DataRequired()])
   submit = SubmitField("Login")

class Search(FlaskForm):
   data = StringField("Search")