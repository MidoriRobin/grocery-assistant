from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    #remember_me = BooleanField('Remember me')


#class ProfileForm(FlaskForm):
#    firstname = StringField('First Name', validators=[DataRequired()])
#    lastname = StringField('Last Name', validators=[DataRequired()])
#    gender = SelectField('Gender', choices=[('M','Male'),('F','Female'),('Othr','Other')], validators=[DataRequired()])
#    email = StringField('Email', validators=[DataRequired(), Email()])
#    pwrd =  PasswordField('Password', validators=[DataRequired()])
#    uname = StringField('Username', validators=[DataRequired()])
