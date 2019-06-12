from flask import Flask


app = Flask(__name__)

"""
1. 先执行 decorator = app.route('/index')   
2. @decorator
"""

@app.route('/index',endpoint='n1',methods=['GET',"POST"])
def index():

    return "index"

@app.route('/new')
def new():
    return "New"

if __name__ == '__main__':
    app.run()