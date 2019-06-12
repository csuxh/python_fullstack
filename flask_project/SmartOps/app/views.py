from flask import Blueprint
from manage import app

main = Blueprint('main',__name__)

@main.route('/')
def main_index():
    return app.send_static_file('index.html')