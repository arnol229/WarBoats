import math
import boats

class Board(object): # Creating a board
    boat_count = None
    def __init__(self, rows, cols):
        self.boat_count = 0
        self.rows = rows
        self.cols = cols
        self.ship_points = []
        self.board = []
        self.gen_board(self.rows, self.cols)
        #print_board(self.Board)

    def add_boat(self, boat):
        self.boats.append(boat)
        self.boat_count += 1

    def lookup(self, boat, x,y):
        if self.check_point(x,y) is False:
            return False
        spots = []
        coords = [(x,y),] # This is the first piece of the ship
        piece = 0
        print "anchor piece set at {} for {} (up)".format(coords, boat.type)
        while piece is not boat.boat_spaces: #while counter has not hit total ship pieces
            piece += 1
            if x - piece >= 0 and self.check_point(x-piece, y) is True:
                coords.append((x-piece, y,))
                if piece is boat.boat_spaces: # if all pieces fit
                    spots.append(coords)# take all the spots appended to coord and put them in spots
                    for coordinates in spots:
                        for xy in coordinates:
                            boat.points.append(boats.ShipPoints(xy[0], xy[1]))
                            self.ship_points.append(boats.ShipPoints(xy[0], xy[1]))
                        # Intended to create a shippoint and append the object to points list in the boat
                    print "ship placed up: {}".format(spots)
                    return True
                    break
            else: # if they cant be placed, reset coords to x,y for the rest of the while loops
                return False

    def lookdown(self, boat, x,y):
        #Check Down
        if self.check_point(x,y) is False:
            return False
        spots = []
        coords = [(x,y),]
        piece = 0
        print "anchor piece set at {} for {} (down)".format(coords, boat.type)
        while piece is not boat.boat_spaces:
            piece += 1
            if x + piece <= self.rows and self.check_point(x+piece, y) is True:
                coords.append((x+piece, y),)
                if piece is boat.boat_spaces:
                    spots.append(coords)
                    for coordinates in spots:
                        for xy in coordinates:
                            boat.points.append(boats.ShipPoints(xy[0], xy[1]))
                            self.ship_points.append(boats.ShipPoints(xy[0], xy[1]))
                    print "ship placed down: {}".format(spots)
                    return True
                    break
            else:
                return False

    def lookleft(self, boat, x,y):
        # Check left
        if self.check_point(x,y) is False:
            return False
        spots = []
        coords = [(x,y),]
        piece = 0
        print "anchor piece set at {} for {} (left)".format(coords, boat.type)
        while piece != boat.boat_spaces:
            piece += 1
            if y - piece >= 0 and self.check_point(x, y-piece) is True:
                coords.append((x, y-piece,),)
                if piece is boat.boat_spaces:
                    spots.append(coords)
                    for coordinates in spots:
                        for xy in coordinates:
                            boat.points.append(boats.ShipPoints(xy[0], xy[1]))
                            self.ship_points.append(boats.ShipPoints(xy[0], xy[1]))
                    print "ship placed left: {}".format(spots)
                    return True
                    break
            else:
                return False

    def lookright(self, boat, x,y):
        # Check right
        if self.check_point(x,y) is False:
            return False
        spots = []
        coords = [(x,y),]
        piece = 0
        print "anchor piece set at {} for {} (right)".format(coords, boat.type)
        while piece != boat.boat_spaces:
            piece += 1
            if y + piece <= self.cols and self.check_point(x, y+piece) is True:
                coords.append((x, y+piece,),)
                if piece is boat.boat_spaces:
                    spots.append(coords)
                    for coordinates in spots:
                        for xy in coordinates:
                            boat.points.append(boats.ShipPoints(xy[0], xy[1]))
                            self.ship_points.append(boats.ShipPoints(xy[0], xy[1]))
                    print "ship placed right: {}".format(spots)
                    return True
                    break
            else:
                return False

    def gen_board(self, rows, cols):
        for row in range(rows):
            self.board.append(["O"] * cols)

    def print_board(self, board):
        for row in self.board:
            print " ".join(row)

    def check_point(self,x,y):
        for point in self.ship_points:
                if x is point.x and y is point.y:
                    print "Error! ship located at {},{}!".format(x,y)
                    return False
        return True

    look_directions = ['lookleft', 'lookright', 'lookup', 'lookdown'] # does this have to be down here?
    # after the functions are defined?