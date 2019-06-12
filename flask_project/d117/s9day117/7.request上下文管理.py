# by luffycity.com
from flask import Flask,request,session
from flask.sessions import SecureCookieSessionInterface
from flask_session import Session
from redis import StrictRedis

redis = StrictRedis(host='127.0.0.1', port=6379)
app = Flask(__name__)

# app.session_interface = SecureCookieSessionInterface()
# app.session_interface = RedisSessionInterface()
app.config['SESSION_TYPE'] = 'redis'
app.config['SESSION_REDIS'] = redis
# app.config['SESSION_PERMANENT'] = False  # 如果设置为True，则关闭浏览器session就失效。
# app.config['SESSION_KEY_PREFIX'] = 'session:'  # 保存到session中的值的前缀

Session(app)

@app.route('/login')
def login():
    session['user'] = 'alex'
    return 'asdfasfd'

@app.route('/home')
def index():
    print(session.get('user'))

    return '...'


if __name__ == '__main__':
    app.run()
    # app.__call__
    # app.wsgi_app