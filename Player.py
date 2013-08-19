class Player(object): # create the player
    self.PlayerID = None #simple 1 or 0 to differentiate players
    self.Name = None
    self.Type = None
    self.MyBoard = None
    self.EnemyBoard = None

	__init__(self, PlayerID, Name, Type): # should i bring in the dictionary entry? probably not?
		self.PlayerID = PlayerID
		self.Name = Name
		self.Type = Type
		self.MyBoard = self.AddBoard("MyBoard", self.PlayerID)

	def AddBoard(self, Type, PlayerID): # generate a enemyboard and myboard
		self.Type = Type
		if self.Type == "MyBoard":
			self.MyBoard = Board("MyBoard" , self.PlayerID)
		elif self.Type =="EnemyBoard":
			self.EnemyBoard = Board("EnemyBoard", self.PlayerID)