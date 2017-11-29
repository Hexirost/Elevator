MAX_EVEVATOR_SIZE = 5

class Elevator():

	def __init__(self, name):
		self.max 		= MAX_EVEVATOR_SIZE
		self.called 	= False 
		self.riders 	= []
		self.name	 	= name
		self.curr_floor	= 0
		self.dest_floor	= 0
		self.stops		= []

	def addRider(self,rider):
		self.riders.append(rider)

	def getRiders(self):
		return self.riders


