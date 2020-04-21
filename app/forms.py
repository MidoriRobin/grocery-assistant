from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
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

class UsrForm(FlaskForm):
    firstname = StringField('First Name', validators=[DataRequired()])
    lastname = StringField('Last Name', validators=[DataRequired()])
    sex = StringField('Sex/Gender', validators=[DataRequired()])
    email=StringField('Email', validators=[DataRequired()])
    phonenumber=StringField('Phone Number', validators=[DataRequired()])
    city= StringField('City', validators=[DataRequired()])
    street= StringField('Street', validators=[DataRequired()])
    hhsize = StringField('HouseHold Size', validators=[DataRequired()])
    adlts = StringField('Number of Adults', validators=[DataRequired()])
    kids = StringField('Number of Kids', validators=[DataRequired()])
    maritalstat=StringField('Marital Status', validators=[DataRequired()])
    dietpref =StringField('Dietary Preference',validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign Up')
