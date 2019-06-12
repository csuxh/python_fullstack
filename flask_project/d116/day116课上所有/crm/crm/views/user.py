from flask import Blueprint

uc = Blueprint('uc',__name__)


@uc.route('/list')
def list():
    return 'List'


@uc.route('/detail')
def detail():
    return 'detail'