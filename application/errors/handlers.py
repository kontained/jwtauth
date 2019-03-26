from flask import jsonify, current_app
from application.auth.exceptions import AuthenticationError, AccountAlreadyExistsError
from . import errors_blueprint


@errors_blueprint.app_errorhandler(AccountAlreadyExistsError)
def handle_account_already_exists_error(error):
    current_app.logger.error(error, exc_info=1)
    response = jsonify(
        {
            'message': 'Account already exists.'
        }
    )
    response.status_code = 400
    return response


@errors_blueprint.app_errorhandler(AuthenticationError)
def handle_authentication_error(error):
    current_app.logger.error(error, exc_info=1)
    response = jsonify(
        {
            'message': 'Account could not be authenticated.'
        }
    )
    response.status_code = 401
    return response


@errors_blueprint.app_errorhandler(Exception)
def handle_exception(error):
    current_app.logger.error(error, exc_info=1)
    response = jsonify(
        {
            'message': 'Internal server error.'
        }
    )
    response.status_code = 500
    return response


@errors_blueprint.app_errorhandler(404)
def handle_not_found(error):
    current_app.logger.error(error, exc_info=1)
    response = jsonify(
        {
            'message': 'Not found.'
        }
    )
    response.status_code = 404
    return response
