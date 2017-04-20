from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,RadioField,IntegerField,PasswordField,BooleanField
from wtforms.validators import DataRequired,Email, EqualTo

class VmMachineForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    ipAddress = StringField('IP Address', validators=[DataRequired()])
    userName = StringField('Username', validators=[DataRequired()])
    password_hs = StringField('Password', validators=[DataRequired()])
    rootName = StringField('Rootname', validators=[DataRequired()])
    passwordRoot_hs = StringField('passwordRoot', validators=[DataRequired()])
    os = RadioField('OS', choices=[('linux','linux'),('windows','windows')])
    ram = IntegerField('ram', validators=[DataRequired()])
    rom = IntegerField('rom', validators=[DataRequired()])
    cpu = IntegerField('cpu', validators=[DataRequired()])
    submit = SubmitField('Add')
class ProgrammeForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    version = StringField('Version', validators=[DataRequired()])
    link = StringField('Link', validators=[DataRequired()])
    submit = SubmitField('Add')
class Config_Notif_Form(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    ram = IntegerField('ram', validators=[DataRequired()])
    rom = IntegerField('rom', validators=[DataRequired()])
    cpu = IntegerField('cpu', validators=[DataRequired()])
    submit = SubmitField('Add')
class User_Form(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    username = StringField('Username', validators=[DataRequired()])
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    password = PasswordField('Password', validators=[
        DataRequired(),
        EqualTo('confirm_password')
    ])
    confirm_password = PasswordField('Confirm Password')
    is_admin = BooleanField('is Admin',default=False)
    submit = SubmitField('Add')
class User_Update_Form(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    username = StringField('Username', validators=[DataRequired()])
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    is_admin = BooleanField('is Admin', default=False)
    submit = SubmitField('Add')
