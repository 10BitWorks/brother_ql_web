from flask import Blueprint

bp = Blueprint('labels', __name__, template_folder='templates')

from . import routes
