from flask import Flask
from logging.config import dictConfig
import os, sys

from .planet import planet_controller
from .ship import ship_controller
from .ticket import ticket_controller



dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://sys.stdout',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})


def create_app():
    app = Flask(__name__)
    app.config.from_mapping(
        DATABASE=os.environ.get('DATABASE_URL')
    )
    app.register_blueprint(planet_controller)
    app.register_blueprint(ship_controller)
    app.register_blueprint(ticket_controller)

    return app