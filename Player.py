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