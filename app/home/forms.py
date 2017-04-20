from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,RadioField,IntegerField,PasswordField,BooleanField,Label
from wtforms.validators import DataRequired,Email, EqualTo


class Form_Ssh(FlaskForm):
    id= StringField('Id',validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Connect')