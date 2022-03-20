


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


@app.route('/tickets')
def list_all_tickets():
        """
        List all tickets on the travel manifest.
        """
        return ''

@app.route('/tickets/{id}')
def get_ticket_by_id(id):
        """
        Get a specific ticket by ID.
        """
        return ''

## POST
@app.route('/tickets')
def add_new_ticket(ticket):
        """
        Buy a ticket to a ship. You're one of the lucky ones.
        """
        return ''