from flask import Flask

app = Flask(__name__)


@app.route('/index')
def index():
    print('index')
    return "Index"


class Middleware(object):
    def __init__(self,old):
        self.old = old

    def __call__(self, *args, **kwargs):
        ret = self.old(*args, **kwargs)
        return ret


if __name__ == '__main__':
    app.wsgi_app = Middleware(app.wsgi_app)
    app.run()
