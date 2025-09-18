from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flasgger import Swagger

db = SQLAlchemy()
jwt = JWTManager()


def create_app(config_overrides=None):
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = 'your-secret-key'

    if config_overrides:
        app.config.update(config_overrides)

    db.init_app(app)
    jwt.init_app(app)
    Swagger(app)

    from .routes import auth_bp
    app.register_blueprint(auth_bp)

    with app.app_context():
        db.create_all()

    return app
