from flask import Flask,render_template,request,redirect,session,url_for,jsonify,make_response,Markup,flash,get_flashed_messages

app = Flask(__name__)

app.config.from_object("settings.DevelopmentConfig")

STUDENT_DICT = {
    1:{'name':'王龙泰','age':38,'gender':'中'},
    2:{'name':'小东北','age':73,'gender':'男'},
    3:{'name':'田硕','age':84,'gender':'男'},
}

# @app.before_request
# def xxxxxx():
#     if request.path == '/login':
#         return None
#
#     if session.get('user'):
#         return None
#
#     return redirect('/login')

@app.template_global()
def sb(a1, a2):
    # {{sb(1,9)}}
    return a1 + a2

# 可以放到if后面做条件
@app.template_filter()
def db(a1, a2, a3):
    # {{ 1|db(2,3) }}
    return a1 + a2 + a3


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

@app.route('/delete/<int:nid>')
def delete(nid):

    del STUDENT_DICT[nid]
    return redirect(url_for('index'))

@app.route('/detail/<int:nid>')
def detail(nid):
    info = STUDENT_DICT[nid]
    return render_template('detail.html',info=info)

def func(arg):
    return arg + 1

@app.route('/tpl')
def tpl():
    context = {
        'users':['longtai','liusong','zhoahuhu'],
        'txt':Markup("<input type='text' />"),
        'func':func
    }

    return render_template('tpl.html',**context)

@app.route('/session')
def sess():
    session['k1'] = 'xxx1'
    session['k2'] = 'xxx2'
    print(session)
    del session['k2']
    print(session)
    return 'session test'

@app.route('/page1')
def page1():
    # session['uuuuu'] = 123
    flash('临时数据存储','error')
    flash('sdfsdf234234','error')
    flash('adasdfasdf','info')
    print(flash)
    return "Session"

@app.route('/page2')
def page2():
    # print(session['uuuuu'])
    # del session['uuuuu']
    # session.pop('uuuuu')
    print(get_flashed_messages(category_filter=['error']))
    return "Session"


@app.errorhandler(404)
def err_page(arg):
    print(arg)
    return '页面没找到'

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000)
