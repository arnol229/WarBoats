class Boat(object):
    self.Alive = True
    self.points = []
    self.BoatSpaces = None

	__init__(self, Type): #bring in type later? battleship,cruiser
		self.Type = Type
		if self.Type = "Destroyer":
			self.BoatSpaces = 2
		if self.Type = "Cruiser":
			self.BoatSpaces = 3
		if self.Type = "WarBoat":
			self.BoatSpaces = 4

		Board.OpenSpots()

	def IsDead(self):
		# check to see if this boat's ship points are all dead

		for point in self.points:
			if point.alive:
				#return early because there is still 1 point alive
				return False
		return True

class ShipPoints(object): #Each ship will be assigned 1 ShipPoint per point of its length
	__init__(self, x, y):
		self.x = x # X coordinate
		self.y = y # Y coordinate
		self.alive = True # Is it alive or dead?