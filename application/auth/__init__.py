from flask import Blueprint


auth_blueprint = Blueprint('auth', __name__)

# routes needs to be below auth_blueprint, so it is importable
from . import routes