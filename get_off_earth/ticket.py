from flask import Blueprint, request
from .db import select_from_db, insert_one
import json


class Ticket:
    def __init__(self, 
                id, 
                planet_id, 
                planet_name, 
                distance, 
                ship_id,
                ship_name, 
                ship_type_id, 
                ship_tye_model_name, 
                trip_time, 
                trip_danger, 
                name, 
                pod_quantity):
        self.id = id
        self.ship_id = ship_id
        self.ship_name = ship_name
        self.ship_type_id = ship_type_id
        self.ship_tye_model_name = ship_tye_model_name
        self.planet_id = planet_id
        self.planet_name = planet_name
        self.distance = distance # Light-years
        self.trip_time = trip_time # Years
        self.trip_danger = trip_danger # High, Medium, Low
        self.name = name
        self.pod_quantity = pod_quantity # How many beds?


class TicketDAO:
    def __init__(self, 
                id, 
                ship_id, 
                name, 
                pod_quantity):
        self.id = id
        self.ship_id = ship_id
        self.name = name
        self.pod_quantity = pod_quantity # How many beds?


def to_ticket(record): 
        return Ticket(
                id = record[0], 
                ship_id = record[1], 
                ship_name = record[2],
                ship_type_id = record[3],
                ship_tye_model_name = record[4],
                planet_id = record[5],
                planet_name = record[6],
                distance = record[7],
                trip_time = record[8],
                trip_danger = record[9],
                name = record[10],
                pod_quantity = record[11]
        ).__dict__



ticket_controller = Blueprint('ticket_controller', __name__)


def select_all_tickets_sql(where_statement):
        return "SELECT t1.id, t1.ship_id, t2.name, t2.ship_type_id, t3.model_name, " \
                + "t2.planet_id, t4.name, t4.distance, t2.trip_time, t2.trip_danger, " \
                + "t1.name, t1.pod_quantity FROM tickets t1 INNER JOIN ships t2 " \
                + "ON t1.ship_id = t2.id INNER JOIN ship_types t3 ON t2.ship_type_id = t3.id " \
                + f"INNER JOIN planets t4 ON t2.planet_id = t4.id {where_statement} " \
                + "GROUP BY t1.id, t2.name, t2.ship_type_id, t3.model_name, t2.planet_id, " \
                + "t4.name, t4.distance, t2.trip_time, t2.trip_danger " \
                + "ORDER BY t1.id ASC"


@ticket_controller.route('/tickets', methods = ['GET', 'POST'])
def tickets():
        if request.method == 'GET':
                """
                List all tickets on the travel manifest.
                """
                return json.dumps(list(map(
                                to_ticket, 
                                select_from_db(
                                        select_all_tickets_sql("")
                                )
                        )), indent=4)
        if request.method == 'POST':
                """
                Buy a ticket to a ship. You're one of the lucky ones.
                """
                new_ticket = TicketDAO(
                        None,
                        request.json['ship_id'],
                        request.json['name'],
                        request.json['pod_quantity']
                )
                insert_one("tickets", (
                        new_ticket.ship_id,
                        new_ticket.name,
                        new_ticket.pod_quantity
                ))
                return json.dumps(new_ticket.__dict__, indent=4)


@ticket_controller.route('/tickets/<id>')
def get_ticket_by_id(id):
        """
        Get a specific ticket by ID.
        """
        try:
                return json.dumps(
                                to_ticket(
                                select_from_db(
                                        select_all_tickets_sql(f"WHERE t1.id = {id}")
                                )[0]
                ), indent=4)
        except IndexError:
                return "Not found."
