from flask import Blueprint

blogs = Blueprint('blogs', __name__)

from app.blogs.views import *