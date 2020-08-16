from flask import Blueprint

admins = Blueprint('admins', __name__)

from app.admins.views import *