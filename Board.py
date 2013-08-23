import math

class Board(object): # Creating a board
    PlayerID = None
    BoatCount = None
    Boats = []
    def __init__(self, Rows, Cols):
        self.BoatCount = 0
        self.Rows = Rows
        self.Cols = Cols
        self.Board = []
        self.Board = self.gen_board(self.Rows, self.Cols)
    def AddBoat(self, Boat):
        self.Boats.append(Boat)
        self.BoatCount += 1
    def lookup(self, Boat, x,y):
        spots = []
        coords = [(x,y),] # This is the first piece of the ship
        piece = 0
        while piece != Boat.BoatSpaces: #while counter has not hit total ship pieces
            piece += 1
            if x - piece >= 0:
                coords.append((x-piece, y,))
                if piece == Boat.BoatSpaces: # if all pieces fit
                    spots.append(coords)# take all the spots appended to coord and put them in spots
                    for coordinates in spots:
                        Boat.points.append(Boat.ShipPoints(coordinates[0], coordinates[1]))
                        # Intended to create a shippoint and append the object to points list in the boat
                    place = True
                    break
            else: # if they cant be placed, reset coords to x,y for the rest of the while loops
                place = False
    def lookdown(self,boat, x,y):
        #Check Down
        spots = []
        coords = [(x,y),]
        piece = 0
        while piece != self.Boat.BoatSpaces:
            piece += 1
            if x + piece <= len(row): # not 100% sure on len(row)
                coords.append((x+piece, y,),)
                if piece == self.Boat.BoatSpaces -1:
                    spots.append(coords)
                    for coordinates in spots:
                        self.boat.points.append(self.boat.ShipPoints(coordinates[0], coordinates[1]))
                    break
            else:
                return False
    def lookleft(self,boat, x,y):
        # Check left
        spots = []
        coords = [(x,y),]
        piece = 0
        while piece != self.Boat.BoatSpaces:
            piece += 1
            if y - piece >= 0:
                coords.append((x, y-piece,),)
                if piece == self.Boat.BoatSpaces -1:
                    spots.append(coords)
                    for coordinates in spots:
                        self.boat.points.append(self.boat.ShipPoints(coordinates[0], coordinates[1]))
                    break
            else:
                return False
    def lookright(self, boat, x,y):
        # Check right
        spots = []
        coords = [(x,y),]
        piece = 0
        while piece != self.Boat.BoatSpaces:
            piece += 1
            if y + piece <= len(col): #not sure about this len(col)
                coords.append((x, y+piece,),)
                if piece == self.Boat.BoatSpaces -1:
                    spots.append(coords)
                    for coordinates in spots:
                        self.boat.points.append(self.boat.ShipPoints(coordinates[0], coordinates[1]))
                    break
            else:
                return False

    def gen_board(self, rows, cols):
        for row in range(rows):
            self.Board.append(["O"] * cols)

    def print_board(self, board):
        for row in board:
            col_list = []
            for col in row:
                col_list.append(col)
        print " ".join(col_list)

    lookoptions = [lookleft, lookright, lookup, lookdown] # does this have to be down here?
    # after the functions are defined?