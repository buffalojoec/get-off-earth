from flask import Blueprint, request
from .db import select_from_db, insert_one
import json


class Ship:
    def __init__(self, 
                id, 
                planet_id, 
                planet_name,
                distance,
                ship_type_id, 
                ship_tye_model_name, 
                max_capacity,
                name, 
                trip_time, 
                trip_danger, 
                passengers):
        self.id = id
        self.planet_id = planet_id
        self.planet_name = planet_name
        self.distance = distance # Light-years
        self.ship_type_id = ship_type_id
        self.ship_tye_model_name = ship_tye_model_name
        self.max_capacity = max_capacity
        self.name = name
        self.trip_time = trip_time # Years
        self.trip_danger = trip_danger # High, Medium, Low
        self.passengers = passengers


class ShipDAO:
    def __init__(self, 
                id, 
                planet_id, 
                ship_type_id, 
                name, 
                trip_time, 
                trip_danger):
        self.id = id
        self.planet_id = planet_id
        self.ship_type_id = ship_type_id
        self.name = name
        self.trip_time = trip_time # Years
        self.trip_danger = trip_danger # High, Medium, Low


class ShipType:
    def __init__(self, 
                id, 
                model_name, 
                hyperspeed_rating,
                max_capacity):
        self.id = id
        self.model_name = model_name
        self.hyperspeed_rating = hyperspeed_rating # trip_time = distance/hyperspeed_rating
        self.max_capacity = max_capacity


def to_ship(record): 
        return ShipDAO(
                record[0], 
                record[1], 
                record[2],
                record[3],
                record[4],
                record[5]
        ).__dict__


def to_ship_type(record): 
        return ShipType(
                record[0], 
                record[1], 
                record[2],
                record[3]
        ).__dict__



ship_controller = Blueprint('ship_controller', __name__)


@ship_controller.route('/ships', methods = ['GET', 'POST'])
def ships():
        if request.method == 'GET':
                """
                List all ships on the travel manifest.
                """
                return json.dumps(list(map(
                                to_ship, 
                                select_from_db("SELECT * FROM ships")
                        )))
        if request.method == 'POST':
                """
                Man your own ship. God speed.
                """
                new_ship = ShipDAO(
                        None,
                        request.json['planet_id'],
                        request.json['ship_type_id'],
                        request.json['name'],
                        request.json['trip_time'],
                        request.json['trip_danger']
                )
                insert_one("ships", (
                        new_ship.planet_id,
                        new_ship.ship_type_id,
                        new_ship.name,
                        new_ship.trip_time,
                        new_ship.trip_danger
                ))
                return json.dumps(new_ship.__dict__)


@ship_controller.route('/ships/<id>')
def ship_by_id(id):
        """
        Get a specific ship by ID.
        """
        return json.dumps(
                        to_ship(
                        select_from_db(f"SELECT * FROM ships WHERE id={id}")[0]
        ))


@ship_controller.route('/shipTypes', methods = ['GET', 'POST'])
def ship_types():
        if request.method == 'GET':
                """
                List all ship types in the engineering blueprints.
                """
                return json.dumps(list(map(
                                to_ship_type, 
                                select_from_db("SELECT * FROM ship_types")
                        )))
        if request.method == 'POST':
                """
                Design a new ship type. I hope you know what you're doing.
                """
                new_ship_type = ShipType(
                        None,
                        request.json['model_name'],
                        request.json['hyperspeed_rating'],
                        request.json['max_capacity']
                )
                insert_one("ship_types", (
                        new_ship_type.model_name,
                        new_ship_type.hyperspeed_rating,
                        new_ship_type.max_capacity
                ))
                return json.dumps(new_ship_type.__dict__)
