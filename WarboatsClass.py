# Prompt Login - if cannot find playerid, create? y/n. skip option to null playerid. store 
# Main Menu:
# Switch login - run login class - reassign self.PlayerID according to name
# Play - sub menu: 1 or two player - sub menu: specials or no - board size & # of boats? = RUN GAME CLASS 
# Credits - display credits
# Exit
# 
# for a game, each player gets assigned 2 boards (one with their ships, one with enemy ships)
# enemy ship board is for firing at, your board to see where enemy has fired
# 
# 


class MainMenu(): # Does this need to be a class?
	Login
	

class login(object): #Does this need to be a class?
	# create dictionary with Login name:password. can we attach a playerid? ex. '0001'
	# do we need to?
	__init__(self, PlayerID, Password)
		self.PlayerID = PlayerID
		self.Password = Password
		self.AllPlayers = [] #dictionary to look up id:password. 
		# if true, assign this player id and store games to his history


class ShipPoints(object): #Each ship will be assigned 1 ShipPoint per point of its length
	__init__(self, x, y):
		self.x = x # X coordinate
		self.y = y # Y coordinate
		self.alive = True # Is it alive or dead?

class Game(object): # Create a game. save these objects to pull up a match history?
	__init__(self, Players, Special, PlayerID, Name)
		self.Players = Players
		self.Special = Special
		self.PlayerID = PlayerID
		self.Name = Name
		self.Winner = False
		if self.Players == 2 and self.Special == False:
			TwoPlayer(False, self.PlayerID)
		elif self.Players == False and self.Special == True:
			TwoPlayer(True, self.PlayerID)
		elif self.Players == 1 and self.Special == True:
			SinglePlayer(True, self.PlayerID)
		elif self.Players == 1 and self.Special == False:
			SinglePlayer(False, self.PlayerID)

	def TwoPlayer(self, Special): #Run a two player game
		self.Special = Special
		if Self.Special == True:
			self.Player1 = Player(self.PlayerID, self.Name, self.Type)
			self.Player2 = Player() #Do I need to intialize self.player1&2 in Game init?
		elif Self.Special == False:
			self.Player1 = Player()
			self.Player2 = Player()

	def SinglePlayer(self, Special): #run a 1 player game
		self.Special = Special
		if self.special == True:
			self.Player1 = Player()
			self.ComputerAI = Player() #ComputerAI
		elif self.special == False:
			self.Player1 = Player()
			self.ComputerAI = Player()

class Boat(object):
	__init__(self, PositionList): #bring in type later? battleship,cruiser
		self.Alive = True #Ship starts off alive
		for i in len(PositionList): # Create a ShipPoint for each point of length
			self.Point[i] = ShipPoints(PositionList[i[0]], PositionList[i[1]])
			# ^^ will that work? creating point1, point2, point3 etc..?
		def AliveOrDead():
			# check to see if this boat's ship points are all dead

class Player(object): # create the player
	__init__(self, PlayerID, Name, Type): # should i bring in the dictionary entry? probably not?
		self.PlayerID = PlayerID
		self.Name = Name
		self.Type = Type
		# AddBoard("enemyboard")
		# AddBoard("MyBoard")

	def AddBoard(self, Type): # generate a enemyboard and myboard
		self.Type = Type
		if self.Type == "MyBoard":
			self.MyBoard = Board("MyBoard" , self.PlayerID)

class Board(object): # Creating a board
	__init__(self, Type, PlayerID)
		self.Type = Type
		self.PlayerID = PlayerID
		self.board = []
		self.BoatCount = 0
		if self.Type = "MyBoard" # Below here is a mess. trying to copy paste functions to make methods in this class
			AddBoat()
		def AddBoat(self, Boat):
			self.Boats.append(Boat())
			self.BoatCount += 1

		def get_board(input):
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

		def acceptable_spots(row_size, col_size):
    		print 'Board Size: {0}x{1}'.format(row_size, col_size)
    		for row in range(row_size):
        		x = row
        		for col in range(col_size):
            		y = col
            # so we have our starting point of
            # (x,y) now we need to find the next point for a 2x1 piece
            # vertical and horizontal
            		anchor_point = (x,y,)
            		if x - 1 >= 0:
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