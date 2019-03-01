from application import create_app
from config import Config


if __name__ == '__main__':
    application = create_app(Config)
    application.run()
