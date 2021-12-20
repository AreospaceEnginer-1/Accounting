from flask_wtf.form import FlaskForm
from wtforms.fields.choices import SelectField
from wtforms.fields.numeric import IntegerField
from wtforms.fields.simple import PasswordField, StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email

class Register(FlaskForm):
   name = StringField("Your Name", validators = [DataRequired()])
   username = StringField("Username", validators = [DataRequired()])
   gender = SelectField("Gender", choices=[('M', 'Male'), ('F', 'Female')])
   age = IntegerField("Age", validators=[DataRequired()])
   address = TextAreaField("Address", validators = [DataRequired(), Email()])
   password = PasswordField("Password", validators = [DataRequired()])
   submit = SubmitField("Register")

class Login(FlaskForm):
   username = StringField("Username", validators = [DataRequired()])
   password = PasswordField("Password", validators = [DataRequired()])
   submit = SubmitField("Login")
