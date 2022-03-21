from flask import Blueprint
from .db import select_from_db
import json



class Planet:
    def __init__(self, 
                id, 
                name, 
                distance,
                ships_bound,
                passengers):
        self.id = id
        self.name = name
        self.distance = distance # Light-years
        self.ships_bound = ships_bound
        self.passengers = passengers


class PlanetDAO:
    def __init__(self, 
                id, 
                name, 
                distance):
        self.id = id
        self.name = name
        self.distance = distance # Light-years


planet_controller = Blueprint('planet_controller', __name__)


@planet_controller.route('/planets')
def list_all_planets():
        """
        List all planets on the navigation panel.
        """
        def to_planets(x): return 
                json.dumps(Planet(
                        x[0], x[1], x[2], x[3], x[4]
                ).__dict__)
        return select_from_db()

@planet_controller.route('/planets/<id>')
def get_planet_by_id(id):
        """
        Get a specific planet by ID.
        """
        return "Test"

## POST
@planet_controller.route('/planets')
def add_new_planet(planet):
        """
        Add a new planet to the navigation panel.
        """
        return "Test"