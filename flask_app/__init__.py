from flask import Flask
from config import Config
from .routes.gpt_routes import gpt_routes

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    app.register_blueprint(gpt_routes, url_prefix='/')
    return app