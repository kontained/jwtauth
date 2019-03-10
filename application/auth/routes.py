from application.auth import auth_blueprint
from application.auth.user import User
from application.auth.authentication import Authentication
from flask import request, jsonify


@auth_blueprint.route('/register', methods=['POST'])
def register():
    auth = Authentication()

    post_data = request.get_json()

    response = auth.register_user(post_data)

    return jsonify(response.to_json())


@auth_blueprint.route('/login', methods=['POST'])
def login():
    auth = Authentication()

    post_data = request.get_json()

    response = auth.login(post_data)

    return jsonify(response.to_json())
