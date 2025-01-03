from flask import Flask
from extensions import db
from config import Config
from routes import init_routes
from flask_migrate import Migrate


def create_app():
    app = Flask(__name__, template_folder='templates', static_folder='static')
    app.config.from_object(Config)

    db.init_app(app)

    init_routes(app)
    Migrate(app, db)


    with app.app_context():
        db.create_all()

    return app
