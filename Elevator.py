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
		self.speed		= [0, 75]
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
				curr_dest=None
				if self.going_up:
					curr_dest = max(self.stops)
				else:
					curr_dest = min(self.stops)

				if curr_dest > self.curr_floor:
					self.curr_floor+= 1
					self.still		= False
					self.going_up	= True
				elif curr_dest < self.curr_floor:
					self.curr_floor-= 1
					self.still		= False
					self.going_up	= False

				for rider in self.riders:
					rider.curr_floor=self.curr_floor
				yield self.env.timeout(1)
			else:
				yield self.env.timeout(1)

	def add_stop(self, stop):
		self.stops.append(stop)

	def remove_stop(self, stop):
		self.stops.remove(stop)

	def add_rider(self,rider):
		self.riders.append(rider)