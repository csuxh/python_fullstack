from flask import Flask, url_for, jsonify, make_response, request, session, redirect, render_template

app = Flask(__name__)
app.secret_key='asdfsf'

STUDENT_DICT = {
    1:{'name':'王龙泰','age':38,'gender':'中'},
    2:{'name':'小东北','age':73,'gender':'男'},
    3:{'name':'田硕','age':84,'gender':'男'},
}

@app.before_request
def auth():
    if request.path == '/login':
        return None

    if session.get('user'):
        return None

    return redirect('/login')

@app.route('/login',methods=["GET","POST"])
def login():
    print('login')
    if request.method == 'GET':
        return render_template('login.html')
    user = request.form.get('user')
    pwd = request.form.get('pwd')
    if user == 'jack' and pwd == '123456':
        session['user'] = user
        return redirect('/index')
    return render_template('login.html',error='用户名或密码错误')

@app.route('/index')
def index():
    print('index')
    return render_template('index.html',stu_dic=STUDENT_DICT)

# @app.route('/index/<int:nid>', methods=['GET', 'POST'], endpoint='xxxx')
# def index(nid):
#     print(nid)
#     print(url_for('hello_world', nid=nid))
#     data = {'name': 'jack', 'id': nid}
#     return jsonify(data)


if __name__ == '__main__':
    app.run()

