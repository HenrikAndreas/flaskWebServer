from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField


# Class that 'replaces' html. It translates into html from python.
class Login(FlaskForm):
    username = StringField('Username')
    password = PasswordField('Password')
    submit = SubmitField('Login')

class Register(FlaskForm):
    username = StringField('Username')
    password = PasswordField('Password')
    confirmPassword = PasswordField('Confirm Password')
    submit = SubmitField("Sign Up")

class Lamp(FlaskForm):
    value = StringField('Lamp')
    submit = SubmitField('Turn on/off lamp')