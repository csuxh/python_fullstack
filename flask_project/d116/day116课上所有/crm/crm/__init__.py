from flask import Flask
from .views.account import ac
from .views.user import uc

def create_app():

    app = Flask(__name__)

    # @app.before_request
    # def x1():
    #     print('app.before_request')



    app.register_blueprint(ac)
    app.register_blueprint(uc,url_prefix='/api')
    return app

