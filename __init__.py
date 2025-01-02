from flask import Flask
from extensions import db
from config import Config
from routes import init_routes
def create_app():
    app = Flask(__name__)
    app.config.from_object(__name__)

    db.init_app(app)

    init_routes(app)

    with app.app_context():
        db.create_all()

    return app