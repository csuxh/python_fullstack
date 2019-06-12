from app.models import User, db
from flask import Flask
from config import CONFIG
from flask_jsonrpc import JSONRPC
from app import create_app

app = Flask(__name__)
config_name = 'development'
app.config.from_object(CONFIG[config_name])

jsonrpc = JSONRPC(app, '/api', enable_web_browsable_api=True, auth_backend=User.authenticate)

db.init_app(app)


@jsonrpc.method('App.hello(name=str)', authenticated=User.check_auth)
def hello(name):
    return u'Hello %s!' % name

config_name = 'development'
@app.route('/')
def index():
    return app.send_static_file('index.html')


from app.soapi import user

if __name__ == '__main__':
    app.run(port=5001)
