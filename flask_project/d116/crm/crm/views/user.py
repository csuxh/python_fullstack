from flask import Blueprint

uc = Blueprint('uc',__name__, template_folder='')


@uc.route('/list')
def list():
    return 'List'


@uc.route('/detail')
def detail():
    return 'detail'