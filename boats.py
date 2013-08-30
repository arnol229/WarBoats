class Boat(object):
    def __init__(self):
        self.alive = True
        self.points = []

    def is_dead(self):
        # check to see if this boat's ship points are all dead
        for point in self.points:
            if point.alive:
                #return early because there is still 1 point alive
                return False
        return True

class Destroyer(Boat):
    def __init__(self):
        self.boat_spaces = 1
        self.id = "D"
        self.cannons = 1
        self.cool_down = 1

class Cruiser(Boat):
    def __init__(self):
        self.boat_spaces = 2
        self.id = "C"
        self.cannons = 1
        self.cool_down = 2

class WarBoat(Boat):
    def __init__(self):
        self.boat_spaces = 3
        self.id = "W"
        self.cannons = 2
        self.cool_down = 4

class ShipPoints(object): #Each ship will be assigned 1 ShipPoint per point of its length
    def __init__(self, x, y):
        self.x = x # X coordinate
        self.y = y # Y coordinate
        self.alive = True # Is it alive or dead?