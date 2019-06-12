from flask import Flask

# 1. 实例化Flask对象
app = Flask(__name__)

# 2. 设置路由
"""
app.url_map = [
    ('/index',index),
    ('/login',login),
]
"""
@app.route('/index')
def index():
    return "index"


if __name__ == '__main__':
    # 3. 启动socket服务端
    app.run()

    # 4. 用户请求到来
    app.__call__
    app.wsgi_app
    app.request_class
    app.session_interface