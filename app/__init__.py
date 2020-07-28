from flask import Flask
from flask_bootstrap import Bootstrap

bootstrap = Bootstrap()

def create_app(config_name):

    app = Flask(__name__)

    Bootstrap(app)

    from .home import home as home_blueprint
    app.register_blueprint(home_blueprint)

    return app