import Board.py

class Player(object): # create the player
    self.Ships = None
    self.Power = None
    self.AI = None
    self.MyBoard = None
    self.EnemyBoard = None

	__init__(self, Power, MyBoard, EnemyBoard, Ships, AI):
		self.AI = AI
		self.Power = Power
		self.Ships = Ships
		#self.EnemyBoard = Board.(EnemyBoard)
		self.MyBoard = Board.GenBoard(MyBoard)

	def place_ship(self, ship, board):
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