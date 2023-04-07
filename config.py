import os

class Config:
    # General Config
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'my-secret'
    FLASK_APP = os.environ.get('FLASK_APP') or 'app.py'
    FLASK_ENV = os.environ.get('FLASK_ENV') or 'development'

    