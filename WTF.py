from flask_wtf.form import FlaskForm
from flask_wtf import RecaptchaField
from wtforms.fields.numeric import IntegerField
from wtforms.fields.simple import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email

class Register(FlaskForm):
   name = StringField("Your Name", validators = [DataRequired()])
   username = StringField("Username", validators = [DataRequired()])
   email = StringField("Username", validators = [DataRequired(), Email()])
   age = IntegerField("Age", validators=[DataRequired()])
   password = PasswordField("Password", validators = [DataRequired()])
   c_password = PasswordField("Password", validators = [DataRequired()])
   recaptcha = RecaptchaField()
   submit = SubmitField("Register")

class Login(FlaskForm):
   username = StringField("Username", validators = [DataRequired()])
   password = PasswordField("Password", validators = [DataRequired()])
   submit = SubmitField("Login")
