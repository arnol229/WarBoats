from math import randint

class Board(object): # Creating a board
	self.Type = None
	self.PlayerID = None
	self.Board = None
	self.BoatCount = None
	self.Boats = None
	__init__(self, Rows, Cols, Type)
		self.Rows = Rows
        self.Cols = Cols
        self.Type = Type
		self.board = []
		self.BoatCount = 0

	def AddBoat(self, Boat):
		self.Boats.append(Boat())
		self.BoatCount += 1

	def get_board(self, input):
		input.lower()
		if input == "create":
    		size = raw_input("please enter the dimensions (format #x#): ")
    		row_size = int(size[0])
    		col_size = int(size[2])
    		print "Generating your board with {} rows and {} collumns...".format(row_size, col_size)
    		gen_board(row_size, col_size)
    		self.OpenSpots = acceptable_spots(row_size, col_size)
    #ship_count = (int(raw_input("How many ships?")))
    		return open_spots
    #print row_size, col_size
		elif input == "random":
    		print "generating random board..."
    		row_size = random.randint(3,10)
    		col_size = random.randint(3,10)
    		gen_board(row_size, col_size)
    		Self.OpenSpots = acceptable_spots(row_size, col_size)
    #ship_count = (int(raw_input("How many ships?")))
    		return open_spots
    #print row_size, col_size
		else:
    		get_board(str(raw_input("error, please retry : Create / Random: ")))

	def acceptable_spots(self, Board, Ship):
		print 'Board Size: {0}x{1}'.format(Board)
		for row in range(Board):
    		x = row
    		for col in range(row):
        		y = col
        # so we have our starting point of
        # (x,y) now we need to find the next point for a 2x1 piece
        # vertical and horizontal
        		anchor_point = (x,y,)
        		if x - self.Ship.length >= 0:
            # checking if the piece can go vertically up 1 spot
            		open_spots.append((anchor_point, (x-1, y,),))
        		if x + 1 <= row_size-1:
            # checking to see if piece can go vertically down 1 spot
            		open_spots.append((anchor_point, (x+1, y,),))
        		if y - 1 >= 0:
            # checking to see if piece can go horizontally left 1 spot
            		open_spots.append((anchor_point, (x, y-1,),))
        		if y + 1 <= col_size-1:
            # checking to see if piece can go horizontally right 1 spot
            		open_spots.append((anchor_point, (x, y + 1,),))

    def gen_board(self, rows, cols):
    	for row in range(rows):
        	self.board.append(["O"] * cols)

    def print_board(self, board):
    	for row in board:
        	col_list = []
        	for col in row:
            	col_list.append(col)
        print " ".join(col_list)

    def place_ship(self, ship_count,open_spots):
    	while ship_count != 0:
        	ship = random.choice(open_spots)
        	remove_spots(open_spots, ship)
        	ship_pos.append(ship)
        	print "ship #{}: {}".format(ship_count, ship)
        	for xy in ship:
            	board[xy[0]][xy[1]] = "{}".format(ship_count)
            	print_board(board)
            	print " "
        	ship_count -= 1