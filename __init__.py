from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    app.config["SECRET_KEY"] = "supersecret"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///push_ups_logger.sqlite"

    db.init_app(app)

    from . import models
    with app.app_context():
        db.create_all()

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    return app
