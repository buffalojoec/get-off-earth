


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