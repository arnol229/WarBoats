class Boat(object):
    self.Alive = True
    self.points = []

	__init__(self, Type, PositionList): #bring in type later? battleship,cruiser
		#for i in len(PositionList): # Create a ShipPoint for each point of length
		#	self.points[i] = ShipPoints(PositionList[i[0]], PositionList[i[1]])
		#	# ^^ will that work? creating point1, point2, point3 etc..?
		for pl in PositionList:
			self.points.append(pl)

	def AliveOrDead(self):
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