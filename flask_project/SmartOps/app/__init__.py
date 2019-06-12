from flask import Flask
from config import CONFIG
from flask_sqlalchemy import SQLAlchemy
# from flask_marshmallow import Marshmallow
from  marshmallow import Schema as Marshmallow
from user import mod

db = SQLAlchemy()
ma = Marshmallow()


def create_app(config_name):
    """Configure the app w.r.t Flask-security, databases, loggers."""
    app = Flask(__name__)
    app.config.from_object(CONFIG[config_name])
    db.init_app(app)
    # ma.init_app(app)
    # jsonrpc.register_blueprint(mod)
    # app.register_blueprint()

    @app.route('/')
    def main_index():
        return app.send_static_file('index.html')

    return app
