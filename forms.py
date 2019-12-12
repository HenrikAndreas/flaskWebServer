from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo

# This python code is being translated into HTML code, that replaces the usual HTML Input / submit fields
class Registration(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=5, max=20)])
    
    email = StringField('Email', validators=[DataRequired(), Email()])

    password = PasswordField('Password', validators=[DataRequired(), Length(min=5)])
    confirmPassword = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])

    SubmitField = SubmitField('Sign Up')
    
class Login(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=5, max=20)])
    
    password = PasswordField('Password', validators=[DataRequired()])

    SubmitField = SubmitField('Login')
