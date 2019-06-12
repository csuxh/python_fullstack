from app import create_app
from app import db
from app.models import User
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand
from flask_jsonrpc import JSONRPC
import os

# app = create_app(os.getenv('FLASK_CONFIG') or 'development')
app = create_app('development')
jsonrpc = JSONRPC(app, '/api', enable_web_browsable_api=True, auth_backend=User.authenticate)
manager = Manager(app)
migrate = Migrate(app, db)


def make_shell_context():
    return dict(app=app, db=db, User=User)


manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)

# 载入jsonrpc的接口
import app.soapi.user
import app.ansible2.api
import app.soapi.asset
import app.soapi.knowledge
import app.soapi.project
# 载入后台模板

if __name__ == '__main__':
    manager.run()
