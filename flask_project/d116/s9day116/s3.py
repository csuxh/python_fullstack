import functools
from flask import Flask,views
app = Flask(__name__)


def wrapper(func):
    @functools.wraps(func)
    def inner(*args,**kwargs):
        return func(*args,**kwargs)

    return inner



class UserView(views.MethodView):
    methods = ['GET']
    decorators = [wrapper,]

    def get(self,*args,**kwargs):
        return 'GET'

    def post(self,*args,**kwargs):
        return 'POST'

app.add_url_rule('/user',None,UserView.as_view('uuuu'))

if __name__ == '__main__':
    app.run()
