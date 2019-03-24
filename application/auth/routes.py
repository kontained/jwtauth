from . import auth_blueprint
from .user import User
from .authentication import Authentication
from flask import request, jsonify


@auth_blueprint.route('/register', methods=['POST'])
def register():
    try:
        auth = Authentication()

        post_data = request.get_json()

        response = auth.register_user(post_data)

        return jsonify(response.to_json())
    except Exception as e:
        pass


@auth_blueprint.route('/login', methods=['POST'])
def login():
    try:
        auth = Authentication()

        post_data = request.get_json()

        response = auth.login(post_data)

        return jsonify(response.to_json())
    except Exception as e:
        pass
