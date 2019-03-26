from . import auth_blueprint
from .authentication import register_user, login_user, authenticate_user
from flask import request, jsonify


@auth_blueprint.route('/register', methods=['POST'])
def register():
    response = register_user(request.get_json())

    return jsonify(response.to_json())


@auth_blueprint.route('/login', methods=['POST'])
def login():
    response = login_user(request.get_json())

    return jsonify(response.to_json())


@auth_blueprint.route('/authenticate', methods=['GET'])
def authenticate():
    response = authenticate_user(request.headers.get('Authorization'))

    return jsonify(response.to_json())
