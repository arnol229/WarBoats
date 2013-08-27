class Boat(object):
    def __init__(self, type):
        self.type = type
        self.boat_spaces = None
        self.alive = True
        self.id = None
        self.points = []
        if self.type == "Destroyer":
            self.boat_spaces = 1
            self.id = "D"
        if self.type == "Cruiser":
            self.boat_spaces = 2
            self.id = "C"
        if self.type == "WarBoat":
            self.boat_spaces = 3
            self.id = "W"

    def is_dead(self):
        # check to see if this boat's ship points are all dead
        for point in self.points:
            if point.alive:
                #return early because there is still 1 point alive
                return False
        return True

class ShipPoints(object): #Each ship will be assigned 1 ShipPoint per point of its length
    def __init__(self, x, y):
        self.x = x # X coordinate
        self.y = y # Y coordinate
        self.alive = True # Is it alive or dead?