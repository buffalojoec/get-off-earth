


class Ship:
    def __init__(self, 
                id, 
                name, 
                planet_id, 
                planet_name,
                distance,
                ship_type_id, 
                ship_tye_model_name, 
                trip_time, 
                trip_danger, 
                max_capacity,
                passengers):
        self.id = id
        self.name = name
        self.planet_id = planet_id
        self.planet_name = planet_name
        self.distance = distance # Light-years
        self.ship_type_id = ship_type_id
        self.ship_tye_model_name = ship_tye_model_name
        self.trip_time = trip_time # Years
        self.trip_danger = trip_danger # High, Medium, Low
        self.max_capacity = max_capacity
        self.passengers = passengers


class ShipDAO:
    def __init__(self, 
                id, 
                name, 
                planet_id, 
                ship_type_id, 
                trip_time, 
                trip_danger, 
                max_capacity):
        self.id = id
        self.name = name
        self.planet_id = planet_id
        self.ship_type_id = ship_type_id
        self.trip_time = trip_time # Years
        self.trip_danger = trip_danger # High, Medium, Low
        self.max_capacity = max_capacity


class ShipType:
    def __init__(self, 
                id, 
                model_name, 
                hyperspeed_rating):
        self.id = id
        self.model_name = model_name
        self.hyperspeed_rating = hyperspeed_rating # trip_time = distance/hyperspeed_rating


@app.route('/ships')
def list_all_ships():
        """
        List all ships on the travel manifest.
        """
        return ''

@app.route('/ships/{id}')
def get_ship_by_id(id):
        """
        Get a specific ship by ID.
        """
        return ''

@app.route('/shipTypes')
def list_all_ship_types():
        """
        List all ship types in the engineering blueprints.
        """
        return ''

@app.route('/shipTypes')
def publish_new_ship_type():
        """
        Design a new ship type. I hope you know what you're doing.
        """
        return ''

@app.route('/ships')
def build_new_ship():
        """
        Man your own ship. God speed.
        """
        return ''

