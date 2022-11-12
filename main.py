from flask import Flask
from init import db, ma, bcrypt, jwt
import os

from controllers.cli_controller import db_commands


def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
    # look to add config file?

    db.init_app(app)
    ma.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)


    app.register_blueprint(db_commands)

    return app