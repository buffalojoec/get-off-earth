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


def to_ship(record): 
        return Ship(
                id = record[0], 
                planet_id = record[1], 
                planet_name = record[2],
                distance = record[3],
                ship_type_id = record[4],
                ship_tye_model_name = record[5], 
                max_capacity = record[6], 
                name = record[7],
                trip_time = record[8],
                trip_danger = record[9],
                passengers = record[10]
        ).__dict__


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


def to_ship_type(record): 
        return ShipType(
                id = record[0], 
                model_name = record[1], 
                hyperspeed_rating = record[2],
                max_capacity = record[3]
        ).__dict__



ship_controller = Blueprint('ship_controller', __name__)


def select_all_ships_sql(where_statement):
        return "SELECT t1.id, t1.planet_id, t2.name, t2.distance, t1.ship_type_id, " \
                + "t3.model_name, t3.max_capacity, t1.name, t1.trip_time, t1.trip_danger, " \
                + "SUM(t4.pod_quantity) passengers FROM ships t1 INNER JOIN planets t2 " \
                + "ON t1.planet_id = t2.id INNER JOIN ship_types t3 ON t1.ship_type_id = t3.id " \
                + f"INNER JOIN tickets t4 ON t1.id = t4.ship_id {where_statement} " \
                + "GROUP BY t1.id, t2.name, t2.distance, " \
                + "t3.model_name, t3.max_capacity ORDER BY t1.id ASC"


@ship_controller.route('/ships', methods = ['GET', 'POST'])
def ships():
        if request.method == 'GET':
                """
                List all ships on the travel manifest.
                """
                return json.dumps(list(map(
                                to_ship, 
                                select_from_db(
                                        select_all_ships_sql("")
                                )
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
                        select_from_db(
                                select_all_ships_sql(f"WHERE t1.id = {id}")
                        )[0]
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
