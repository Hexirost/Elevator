MAX_EVEVATOR_SIZE = 5

class Elevator():

	def __init__(self, name, env):
		self.max 		= MAX_EVEVATOR_SIZE
		self.riders 	= []
		self.name	 	= name
		self.curr_floor	= 0
		self.stops		= []
		self.going_up	= True
		self.env		= env

	def addRider(self,rider):
		self.riders.append(rider)

	def getRiders(self):
		return self.riders

	def run(self):
		while True:
			if self.stops:
				if self.stops[0] and self.stops[0] > self.curr_floor:
					self.curr_floor+=1
					print "going up"
				elif self.stops[0] and self.stops[0] < self.curr_floor:
					self.curr_floor-=1
					print "going down"
				for rider in self.riders:
					rider.curr_floor=self.curr_floor
					print "moving riders"
				yield self.env.timeout(1)
			else:
				yield self.env.timeout(1)

	def add_stop(self, stop):
		self.stops.append(stop)

	def remove_stop(self, stop):
		try:
			self.stops.remove(stop)
		except:
			pass

	def add_rider(self,rider):
		self.riders.append(rider)