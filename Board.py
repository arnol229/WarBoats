from math import randint

class Board(object): # Creating a board
	self.Type = None
	self.PlayerID = None
	self.Board = None
	self.BoatCount = None
	self.Boats = []
	__init__(self, Rows, Cols, Type)
		self.Rows = Rows
        self.Cols = Cols
        self.Type = Type
		self.board = []
		self.BoatCount = 0

	def AddBoat(self, Boat):
		self.Boats.append(Boat())
		self.BoatCount += 1

    def GiveBoard(self, Board):
        self.BoardReturn = []
        self.Board = Board
        for row in self.Board:


	def get_board(self, input):
		input.lower()
		if input == "create":
    		size = raw_input("please enter the dimensions (format #x#): ")
    		row_size = int(size[0])
    		col_size = int(size[2])
    		print "Generating your board with {} rows and {} collumns...".format(row_size, col_size)
    		gen_board(row_size, col_size)
    		self.open_spots = acceptable_spots(row_size, col_size)
    #ship_count = (int(raw_input("How many ships?")))
    		return open_spots
    #print row_size, col_size
		elif input == "random":
    		print "generating random board..."
    		row_size = random.randint(3,10)
    		col_size = random.randint(3,10)
    		gen_board(row_size, col_size)
    		self.open_spots = acceptable_spots(row_size, col_size)
    #ship_count = (int(raw_input("How many ships?")))
    		return self.open_spots
    #print row_size, col_size
		else:
    		get_board(str(raw_input("error, please retry : Create / Random: ")))

	def open_spots(self, Boat, Board):
        spots = []

        for row in range(self.Board):
            x = row
            for col in range(row):
                y = col
                piece = 0 # counter to place all ship pieces
                coords = [(x,y,),]

                #Check to Up
                while piece != self.Boat.BoatSpaces -1: #while counter has not hit total ship pieces
                    piece += 1 #              we minus one because coords starts with the first ship piece
                    if x - piece >= 0:
                        coords.append((x-piece, y,))
                        if piece == self.Boat.BoatSpaces -1: # if all pieces fit
                            spots.append(coords)# take all the spots appended to coord and put them in spots
                            coords = [(x,y,),]# then reset coords to x,y for the other while loops
                            break
                    else: # if they cant be placed, reset coords to x,y for the rest of the while loops
                        coords = [(x,y,),]
                        break
                piece = 0 # reset counter for next loop

                #Check to the Down
                while piece != self.Boat.BoatSpaces
                    piece += 1
                    if x + piece <= len(row): # not 100% sure on len(row)
                        coords.append((x+piece, y,),)
                        if piece == self.Boat.BoatSpaces -1:
                            spots.append(coords)
                            coords = [(x,y,),]
                            break
                    else:
                        coords = [(x,y,),]
                        break
                piece = 0

                # Check left
                while piece != self.Boat.BoatSpaces
                    piece += 1
                    if y - piece >= 0:
                        coords.append((x, y-piece,),)
                        if piece == self.Boat.BoatSpaces -1:
                            spots.append(coords)
                            coords = [(x,y,),]
                            break
                    else:
                        coords = [(x,y,),]
                        break
                piece = 0

                # Check right
                while piece != self.Boat.BoatSpaces
                    piece += 1
                    if y + piece <= len(col): #not sure about this len(col)
                        coords.append((x, y+piece,),)
                        if piece == self.Boat.BoatSpaces -1:
                            spots.append(coords)
                            coords = [(x,y,),]
                            break
                    else:
                        coords = [(x,y,),]
                        break
                piece = 0

        return spots

    def gen_board(self, rows, cols):
    	for row in range(rows):
        	self.board.append(["O"] * cols)

    def print_board(self, board):
    	for row in board:
        	col_list = []
        	for col in row:
            	col_list.append(col)
        print " ".join(col_list)