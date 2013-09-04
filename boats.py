class Boat(object):

    def is_dead(self):
        # check to see if this boat's ship points are all dead
        for point in self.points:
            if point.alive:
                #return early because there is still 1 point alive
                return False
        return True

    def fire(self):
        x = input("Fire at X: ")
        y = input("Fire at Y: ")
        return x-1,y-1

    def check_point(self,x,y):
        for point in self.points:
            if x is point.x and y is point.y:
                #print "Error! ship located at {},{}!".format(x,y)
                return True
        return False
    
    def kill_point(self,x,y):
        for point in self.points:
            if x is self.point.x and y is self.point.y:
                self.point.alive is False

class Destroyer(Boat):
    def __init__(self):
        self.points = []
        self.boat_spaces = 1
        self.id = "D"
        self.cannons = 1
        self.cooldown = 1
        self.energy = 0

class Cruiser(Boat):
    def __init__(self):
        self.points = []
        self.boat_spaces = 2
        self.id = "C"
        self.cannons = 1
        self.cooldown = 2
        self.energy = 0

class WarBoat(Boat):
    def __init__(self):
        self.points = []
        self.boat_spaces = 3
        self.id = "W"
        self.cannons = 2
        self.cooldown = 4
        self.energy = 0

class ShipPoints(object): #Each ship will be assigned 1 ShipPoint per point of its length
    def __init__(self, x, y):
        self.x = x # X coordinate
        self.y = y # Y coordinate
        self.alive = True # Is it alive or dead?