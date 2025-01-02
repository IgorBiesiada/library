from flask import Blueprint, render_template, request, redirect
from extensions import db


main_bp = Blueprint('main', __name__, template_folder='templates', static_folder='static')

@main_bp.route('/')
def get_base():
    return render_template('base.html')


def init_routes(app):
    app.register_blueprint(main_bp)