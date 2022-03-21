from flask import Flask
import os

from .planet import planet_controller
from .ship import ship_controller
from .ticket import ticket_controller



def create_app():
    app = Flask(__name__)
    app.config.from_mapping(
        DATABASE=os.environ.get('DATABASE_URL')
    )
    app.register_blueprint(planet_controller)
    app.register_blueprint(ship_controller)
    app.register_blueprint(ticket_controller)

    return app