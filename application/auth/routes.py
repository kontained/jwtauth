from . import auth_blueprint
from .user import User
from .authentication import register_user, login_user
from flask import request, jsonify


@auth_blueprint.route('/register', methods=['POST'])
def register():
    post_data = request.get_json()

    response = register_user(post_data)

    return jsonify(response.to_json())


@auth_blueprint.route('/login', methods=['POST'])
def login():
    post_data = request.get_json()

    response = login_user(post_data)

    return jsonify(response.to_json())
