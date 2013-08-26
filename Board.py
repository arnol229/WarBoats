import math
import boats

class Board(object): # Creating a board
    boat_count = None
    boats = []
    def __init__(self, rows, cols):
        self.boat_count = 0
        self.rows = rows
        self.cols = cols
        self.board = []
        self.board = self.gen_board(self.rows, self.cols)
        #print_board(self.Board)

    def add_boat(self, boat):
        self.boats.append(boat)
        self.boat_count += 1

    def lookup(self, boat, x,y):
        spots = []
        coords = [(x,y),] # This is the first piece of the ship
        piece = 0
        while piece is not boat.boat_spaces: #while counter has not hit total ship pieces
            piece += 1
            if x - piece >= 0:
                coords.append((x-piece, y,))
                if piece is boat.boat_spaces: # if all pieces fit
                    spots.append(coords)# take all the spots appended to coord and put them in spots
                    for coordinates in spots:
                        boat.points.append(boats.ShipPoints(coordinates[0], coordinates[1]))
                        # Intended to create a shippoint and append the object to points list in the boat
                    return True
                    break
            else: # if they cant be placed, reset coords to x,y for the rest of the while loops
                return False

    def lookdown(self, boat, x,y):
        #Check Down
        spots = []
        coords = [(x,y),]
        piece = 0
        while piece is not boat.boat_spaces:
            piece += 1
            if x + piece <= self.rows: # not 100% sure on len(row)
                coords.append((x+piece, y,),)
                if piece is boat.boat_spaces:
                    spots.append(coords)
                    for coordinates in spots:
                        boat.points.append(boats.ShipPoints(coordinates[0], coordinates[1]))
                    return True
                    break
            else:
                return False

    def lookleft(self, boat, x,y):
        # Check left
        spots = []
        coords = [(x,y),]
        piece = 0
        while piece != boat.boat_spaces:
            piece += 1
            if y - piece >= 0:
                coords.append((x, y-piece,),)
                if piece is boat.boat_spaces:
                    spots.append(coords)
                    for coordinates in spots:
                        boat.points.append(boats.ShipPoints(coordinates[0], coordinates[1]))
                    return True
                    break
            else:
                return False

    def lookright(self, boat, x,y):
        # Check right
        spots = []
        coords = [(x,y),]
        piece = 0
        while piece != boat.boat_spaces:
            piece += 1
            if y + piece <= self.cols: #not sure about this len(col)
                coords.append((x, y+piece,),)
                if piece is boat.boat_spaces:
                    spots.append(coords)
                    for coordinates in spots:
                        boat.points.append(boats.ShipPoints(coordinates[0], coordinates[1]))
                    return True
                    break
            else:
                return False

    def gen_board(self, rows, cols):
        for row in range(rows):
            self.board.append(["O"] * cols)

    def print_board(self):
        col_list = []
        for row in range(self.rows):
            for col in row:
                col_list.append(col)
        print " ".join(col_list)

    look_directions = [lookleft, lookright, lookup, lookdown] # does this have to be down here?
    # after the functions are defined?