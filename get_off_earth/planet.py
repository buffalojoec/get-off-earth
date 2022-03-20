


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


@app.route('/planets')
def list_all_planets():
        """
        List all planets on the navigation panel.
        """
        return ''

@app.route('/planets/{id}')
def get_planet_by_id(id):
        """
        Get a specific planet by ID.
        """
        return ''

## POST
@app.route('/planets')
def add_new_planet(planet):
        """
        Add a new planet to the navigation panel.
        """
        return ''