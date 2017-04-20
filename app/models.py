import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app import db, login_manager
from collections import OrderedDict

class DictSerializable(object):
    def dump_datetime(table, value):
        if value is None:
            return None
        return [value.strftime("%Y-%m-%d %H:%M:%S")]
    def _asdict(self):
        result = OrderedDict()
        for key in self.__mapper__.c.keys():
            result[key] = getattr(self, key)
        return result
class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(60), index=True, unique=True)
    username = db.Column(db.String(60), index=True, unique=True)
    first_name = db.Column(db.String(60), index=True)
    last_name = db.Column(db.String(60), index=True)
    password_hash = db.Column(db.String(128))
    is_admin = db.Column(db.Boolean, default=False)

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute.')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User: {}>'.format(self.username)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class VM_Programme(db.Model,DictSerializable):
    __tablename__ = 'vm_programmes'
    VirtualMachines_id = db.Column(db.Integer, db.ForeignKey('virtualmachines.id'), primary_key=True)
    Programme_id = db.Column(db.Integer, db.ForeignKey('programme.id'), primary_key=True)
    date_install = db.Column(db.DateTime)
    virtualMachines = db.relationship("Programme")

class VmMachine(db.Model,DictSerializable):
    __tablename__ = 'virtualmachines'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200),index=True, unique=True)
    ipAddress = db.Column(db.String(15),index=True, unique=True)
    userName = db.Column(db.String(60))
    password_hs = db.Column(db.String(128))
    rootName = db.Column(db.String(200))
    passwordRoot_hs = db.Column(db.String(128))
    os = db.Column(db.String(60))
    last_updated = db.Column(db.DateTime ,default=datetime.datetime.now())
    ram = db.Column(db.Integer)
    rom = db.Column(db.Integer)
    cpu = db.Column(db.Integer)
    vm_prog = db.relationship("VM_Programme")
    config_notify_id = db.Column(db.Integer, db.ForeignKey('config_notify.id'))

class Programme(db.Model):
    __tablename__ = 'programme'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True)
    version = db.Column(db.String(60))
    link = db.Column(db.String(60))

    def __repr__(self):
        return '<Programme: {}>'.format(self.name)

class ConfigNotification(db.Model):
    __tablename__ = 'config_notify'
    id = db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(60),unique=True)
    ram = db.Column(db.Integer)
    rom = db.Column(db.Integer)
    cpu = db.Column(db.Integer)
    virtualMachines = db.relationship('VmMachine', backref='confignotification',
                                lazy='dynamic')
    def __repr__(self):
        return '<ConfigNotification: {}>'.format(self.name)
