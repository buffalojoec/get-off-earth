from flask import Blueprint, request
from .db import select_from_db, insert_one
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


def to_planet(record): 
                return PlanetDAO(
                        record[0], 
                        record[1], 
                        record[2]
                ).__dict__



planet_controller = Blueprint('planet_controller', __name__)


@planet_controller.route('/planets', methods = ['GET', 'POST'])
def planets():
        if request.method == 'GET':
                """
                List all planets on the navigation panel.
                """
                return json.dumps(list(map(
                                to_planet, 
                                select_from_db("SELECT * FROM planets")
                        )))
        if request.method == 'POST':
                """
                Add a new planet to the navigation panel.
                """
                new_planet = PlanetDAO(
                        None,
                        request.json['name'],
                        request.json['distance']
                )
                insert_one("planets", (
                        new_planet.name, 
                        new_planet.distance
                        ))
                return json.dumps(new_planet.__dict__)
        

@planet_controller.route('/planets/<id>')
def planet_by_id(id):
        """
        Get a specific planet by ID.
        """
        return json.dumps(
                        to_planet(
                        select_from_db(f"SELECT * FROM planets WHERE id={id}")[0]
        ))
