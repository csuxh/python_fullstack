from flask import Blueprint,render_template

ac = Blueprint('ac', __name__)

@ac.before_request
def x1():
    print('app.before_request')


@ac.route('/login')
def login():
    return render_template('login.html')


@ac.route('/logout')
def logout():
    return 'Logout'