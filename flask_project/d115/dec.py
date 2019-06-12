from flask import Flask
app = Flask(__name__)

@app.before_first_request
def x1():
    print('123123')


@app.route('/index')
def index():
    print('index')
    return "Index"


@app.route('/order')
def order():
    print('order')
    return "order"


@app.errorhandler(404)
def not_found(arg):
    print(arg)
    return "没找到"


if __name__ == '__main__':

    app.run()
