from flask import Blueprint

ssh = Blueprint('ssh', __name__)

from . import views