from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,RadioField,IntegerField,PasswordField,BooleanField,Label
from wtforms.validators import DataRequired,Email, EqualTo


class Form_Shh(FlaskForm):
    ip = Label('IP','ip')
    username = Label('Usename','username')
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Connect')