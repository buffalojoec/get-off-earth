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
                return Planet(
                        id = record[0], 
                        name = record[1], 
                        distance = record[2], 
                        ships_bound = record[3], 
                        passengers = record[4]
                ).__dict__





planet_controller = Blueprint('planet_controller', __name__)


def select_all_planets_sql(where_statement):
        return "SELECT t1.id, t1.name, t1.distance, COUNT(t2.id) ships_bound, SUM(t3.pod_quantity)" \
        + "passengers FROM planets t1 INNER JOIN ships t2 ON t1.id = t2.planet_id " \
        + f"INNER JOIN tickets t3 ON t2.id = t3.ship_id {where_statement} GROUP BY t1.id " \
        + "ORDER BY t1.id ASC"


@planet_controller.route('/planets', methods = ['GET', 'POST'])
def planets():
        if request.method == 'GET':
                """
                List all planets on the navigation panel.
                """
                return json.dumps(list(map(
                                to_planet, 
                                select_from_db(
                                        select_all_planets_sql("")
                                )
                        )), indent=4)
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
                return json.dumps(new_planet.__dict__, indent=4)
        

@planet_controller.route('/planets/<id>')
def planet_by_id(id):
        """
        Get a specific planet by ID.
        """
        try:
                return json.dumps(
                                to_planet(
                                select_from_db(
                                        select_all_planets_sql(f"WHERE t1.id = {id}")
                                )[0]
                ), indent=4)
        except IndexError:
                return "Not found."
