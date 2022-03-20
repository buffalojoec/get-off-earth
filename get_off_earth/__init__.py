from flask import Flask
import os


def create_app():
    app = Flask(__name__)
    app.config.from_mapping(
        DATABASE=os.environ.get('DATABASE_URL')
    )

    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    return app