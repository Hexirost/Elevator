import random

class Rider():

	def __init__(self, name, env):
		self.wait				= random.randint(1,5)
		self.name				= name
		self.chosen_elevator	= None
		self.env				= env
		self.curr_floor 		= 0
		self.desired_floor		= random.randint(1,7)
		self.request_elevator	= False
		self.waiting 			= True
		self.rect				= None
		self.img				= None

	def set_rect(self,rect):
		self.rect = rect

	def set_img(self,img):
		self.img = img

	def run(self):
		while True:
			if not self.waiting:
				if self.curr_floor != self.desired_floor or self.request_elevator:
					if self.request_elevator:
						yield self.env.timeout(1)
					elif self.curr_floor != self.desired_floor and not self.request_elevator and not self.chosen_elevator:
						yield self.env.timeout(1)
					yield self.env.timeout(1)
				elif self.curr_floor == self.desired_floor:
					yield self.env.timeout(self.wait)
					self.desired_floor = random.randint(1,10)
			else:
				yield self.env.timeout(1)
				self.waiting = False
