from flask import Flask
from flask_jsonrpc import JSONRPC
from flask_sqlalchemy import SQLAlchemy
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
import werkzeug

app = Flask(__name__)


def authenticate(f, f_check_auth):
    @wraps(f)
    def _f(*args, **kwargs):
        is_auth = False
        try:
            creds = args[:2]
            is_auth = f_check_auth(creds[0], creds[1])
            if is_auth:
                args = args[2:]
        except IndexError:
            if 'token' in kwargs:
                is_auth = f_check_auth(kwargs['token'])
                if is_auth:
                    kwargs.pop('token')
            else:
                raise Exception('Authenticated methods require at least '
                                         '[token] or {token: } arguments')
            # InvalidParamsError
        if not is_auth:
            raise Exception() #InvalidCredentialsError
        return f(*args, **kwargs)

    return _f


jsonrpc = JSONRPC(app, '/api', enable_web_browsable_api=True, auth_backend=authenticate)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SECRET_KEY'] = '1q2w3e'
app.debug = True
db = SQLAlchemy(app)
from functools import wraps


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password_hash = db.Column(db.String(164))

    def password(self, password):
        """
        设置密码hash值
        """
        self.password_hash = werkzeug.security.generate_password_hash(password)

    def verify_password(self, password):
        """
        将用户输入的密码明文与数据库比对
        """
        print(self.username)

        if self.password_hash:
            return werkzeug.security.check_password_hash(self.password_hash, password)
        return None

    def generate_auth_token(self, expiration=600):
        s = Serializer(app.config['SECRET_KEY'], expires_in=expiration)
        return bytes.decode(s.dumps({'id': self.id}))

    @staticmethod
    def verify_auth_token(token):
        s = Serializer(app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except SignatureExpired:
            return None  # valid token, but expired
        except BadSignature:
            return None  # invalid token
        user = User.query.get(data['id'])
        return user

    def __init__(self, username):
        self.username = username

    def __repr__(self):
        return '<User %r>' % self.username


@jsonrpc.method('user.register(username=str,password=str)')
def user_register(username, password):
    if not User.query.filter_by(username=username).first():
        user = User(username=username)
        user.password(password)
        db.session.add(user)
        db.session.commit()
        return {'status': 0, 'message': u'registe success'}
    else:
        return {'status': 1, 'message': u'user already exists'}


@jsonrpc.method('user.verify(username=str,password=str)')
def user_verify(username, password):
    user = User.query.filter_by(username=username).first()
    if not user:
        return {'status': 1, 'message': u'user not exist'}
    if user.verify_password(password):
        token = user.generate_auth_token()
        return {'status': 0, 'message': u'Welcome%s' % username, 'token': token}
    return {'status': 1, 'message': u'wrong password'}


def check_auth(token):
    #启用debug模式不需要进行token认证
    if app.debug:
        return True
    user = User.verify_auth_token(token)
    if user:
        return True
    return False


@jsonrpc.method('App.hello(name=str)', authenticated=check_auth)
def index(name):
    return u'Hello %s!' % name


if __name__ == '__main__':
    app.run(port=2001)