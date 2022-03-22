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
        self.planet_id = planet_id
        self.planet_name = planet_name
        self.distance = distance # Light-years
        self.ship_id = ship_id
        self.ship_name = ship_name
        self.ship_type_id = ship_type_id
        self.ship_tye_model_name = ship_tye_model_name
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
        return TicketDAO(
                record[0], 
                record[1], 
                record[2],
                record[3]
        ).__dict__



ticket_controller = Blueprint('ticket_controller', __name__)


@ticket_controller.route('/tickets', methods = ['GET', 'POST'])
def tickets():
        if request.method == 'GET':
                """
                List all tickets on the travel manifest.
                """
                return json.dumps(list(map(
                                to_ticket, 
                                select_from_db("SELECT * FROM tickets")
                        )))
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
                return json.dumps(new_ticket.__dict__)


@ticket_controller.route('/tickets/<id>')
def get_ticket_by_id(id):
        """
        Get a specific ticket by ID.
        """
        return json.dumps(
                        to_ticket(
                        select_from_db(f"SELECT * FROM tickets WHERE id={id}")[0]
        ))
