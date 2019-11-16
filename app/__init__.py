from flask import Flask

from app import api
from app.db import close_db


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    app.teardown_appcontext(close_db)

    app.register_blueprint(api.api_blueprint)

    @app.route('/')
    def hello():
        return 'Hello, World!'

    return app
