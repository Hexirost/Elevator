import random

class Rider():

	def __init__(self, name, env):
		self.wait				= random.randint(1,5)
		self.name				= name
		self.chosen_elevator	= None
		self.env				= env
		self.curr_floor 		= 0
		self.desired_floor		= random.randint(1,10)
		self.request_elevator	= False


	def post(self):
		return ("Hello my name is " + str(self.name))

	def run(self):
		while True:
			if self.curr_floor != self.desired_floor or self.request_elevator:
				if self.request_elevator:
					yield self.env.timeout(1)
				if self.curr_floor != self.desired_floor and not self.request_elevator and not self.chosen_elevator:
					yield self.env.timeout(1)
				yield self.env.timeout(1)
			elif self.curr_floor == self.desired_floor:
				yield self.env.timeout(self.wait)
				self.desired_floor = random.randint(1,10)
			else:
				print "Rider waiting for elevator to come" 
				yield self.env.timeout(1)