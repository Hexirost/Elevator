MAX_EVEVATOR_SIZE = 5

class Elevator():

	def __init__(self, name, env):
		self.max 		= MAX_EVEVATOR_SIZE
		self.riders 	= []
		self.name	 	= name
		self.curr_floor	= 0
		self.stops		= []
		self.going_up	= True
		self.still 		= True
		self.env		= env
		self.speed		= [0, 50]
		self.rect		= None
		self.img		= None

	def addRider(self,rider):
		self.riders.append(rider)

	def getRiders(self):
		return self.riders

	def set_rect(self,rect):
		self.rect = rect

	def set_img(self,img):
		self.img = img

	def run(self):
		while True:
			self.still = True
			if self.stops:
				if self.stops[0] and self.stops[0] > self.curr_floor:
					self.curr_floor+= 1
					self.still		= False
					self.going_up	= True
					print "going up",self.name,self.curr_floor
				elif self.stops[0] and self.stops[0] < self.curr_floor:
					self.curr_floor-= 1
					self.still		= False
					self.going_up	= False
					print "going down",self.name,self.curr_floor
				else:
					print "still",self.name,self.curr_floor
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
			"Failed to remove stop"

	def add_rider(self,rider):
		self.riders.append(rider)