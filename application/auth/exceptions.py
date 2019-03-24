class AuthenticationError(Exception):
    pass


class AccountAlreadyExistsError(AuthenticationError):
    pass
