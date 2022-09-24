from flask import Blueprint

welcome = Blueprint('welcome', __name__, template_folder='templates')


@welcome.route('/')
def hello():
    return 'My First API !!'


