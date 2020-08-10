from flask import Blueprint

api = Blueprint('api', __name__)

from .services import user