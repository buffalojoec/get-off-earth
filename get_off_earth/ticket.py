


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
        self.trip_time = trip_time
        self.trip_danger = trip_danger
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