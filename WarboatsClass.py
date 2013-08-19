class MainMenu():
	Login
	

class login(object):
	__init__(self, PlayerID, Password)
		self.PlayerID = PlayerID
		self.Password = Password
		self.AllPlayers = []


class ShipPoints(object):
	__init__(self, x, y):
		self.x = x
		self.y = y
		self.alive = True

class Game(object):
	__init__(self, Players, Special)
		self.Players = Players
		self.Special = Special
		if self.Players == 2 and self.Special == False:
			TwoPlayer(False)
		elif self.Players == False and self.Special == True:
			TwoPlayer(True)
		elif self.Players == 1 and self.Special == True:
			SinglePlayer(True)
		elif self.Players == 1 and self.Special == False:
			SinglePlayer(False)

	def TwoPlayer(self, Special):
		self.Special = Special
		if Self.Special == True

	def SinglePlayer(self, Special):
		self.Special = Special


class Boat(object):
	__init__(self, positionList):
		for i in len(positionList):
			self.point[i] = ShipPoints(positionList[i[0]], positionList[i[1]])

class Player(object):
	__init__(self, PlayerID, Name, Type):
		self.PlayerID = PlayerID
		self.Name = Name
		self.Type = Type

	def AddBoard(self, Type):
		self.Type = Type
		if self.Type == "MyBoard":
			self.MyBoard = Board("MyBoard" , self.PlayerID)

class Board(object):
	__init__(self, Type, PlayerID)
		self.Type = Type
		self.PlayerID = PlayerID
		self.board = []
		self.BoatCount = 0
		if self.Type = "MyBoard"
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