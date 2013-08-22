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

	def place_ship(self, ship):
		shuffle(Board.self.lookoptions)
		#######
		Board.self.lookoptions[0](ship, randint(0,WarBoats.rows), randint(0,Warboats.cols)) #will this work?
		##########
		for f in Board.self.lookoptions:
			f(self, ship,randint(0,WarBoats.rows), randint(0,Warboats.cols))
			# or will this work.. need to write
			# something to try next one if fails
			# or stop the for loop if lookoptions succeeds