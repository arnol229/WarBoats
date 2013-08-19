class Game(object): # Create a game. save these objects to pull up a match history?
	__init__(self, Players, Special, PlayerID, Name)
		self.Players = Players
		self.Special = Special
		self.PlayerID = PlayerID
		self.Name = Name
		self.Winner = False
		if self.Players == 2 and self.Special == False:
			self.TwoPlayer(False, self.PlayerID)
		elif self.Players == False and self.Special == True:
			self.TwoPlayer(True, self.PlayerID)
		elif self.Players == 1 and self.Special == True:
			self.SinglePlayer(True, self.PlayerID)
		elif self.Players == 1 and self.Special == False:
			self.SinglePlayer(False, self.PlayerID)

	def TwoPlayer(self, Special, PlayerID): #Run a two player game
		self.Special = Special
		if Self.Special == True:
			self.Player1 = Player(self.PlayerID, self.Name, self.Type)
			self.Player2 = Player() #Do I need to intialize self.player1&2 in Game init?
		elif Self.Special == False:
			self.Player1 = Player()
			self.Player2 = Player()

	def SinglePlayer(self, Special, PlayerID): #run a 1 player game
		self.Special = Special
		if self.special == True:
			self.Player1 = Player()
			self.ComputerAI = Player() #ComputerAI
		elif self.special == False:
			self.Player1 = Player()
			self.ComputerAI = Player()