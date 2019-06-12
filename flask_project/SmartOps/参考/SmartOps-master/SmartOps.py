from app.models import User, db
from flask import Flask
from .config import CONFIG
from flask_jsonrpc import JSONRPC

app = Flask(__name__)
config_name = 'development'
app.config.from_object(CONFIG[config_name])

jsonrpc = JSONRPC(app, '/api', enable_web_browsable_api=True, auth_backend=User.authenticate)

db.init_app(app)


@jsonrpc.method('App.hello(name=str)', authenticated=User.check_auth)
def hello(name):
    return u'Hello %s!' % name


@app.route('/')
def index():
    return app.send_static_file('index.html')


import soapi.user

if __name__ == '__main__':
    app.run(port=3001)
