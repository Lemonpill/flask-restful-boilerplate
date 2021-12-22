from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from werkzeug.exceptions import HTTPException
from .logger import Log


db = SQLAlchemy()
log = Log()
migrate = Migrate()
limiter = Limiter(key_func=get_remote_address)


def create_app(c):
    app = Flask(__name__)
    app.config.from_object(c)
    db.init_app(app)
    migrate.init_app(app, db)
    limiter.init_app(app)

    from .exceptions.handlers import http
    from .endpoints.swagger import swagger
    from .endpoints.auth import auth
    from .endpoints.users import users

    app.register_error_handler(HTTPException, http)
    app.register_blueprint(swagger, url_prefix="/swagger")
    app.register_blueprint(auth, url_prefix="/auth")
    app.register_blueprint(users, url_prefix="/users")

    return app