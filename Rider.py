import random

class Rider():

	def __init__(self, name, env):
		self.wait			= random.randint(1,5)
		self.level			= 0
		self.dest			= random.randint(0,10) 
		self.name			= name 
		self.env			= env
		self.curr_floor 	= 0
		self.desired_floor 	= 0

	def post(self):
		return ("Hello my name is " + str(self.name))

	def run(self):
		while True:
			print "At", self.env.now, "Rider", self.name, "is waiting..."
			yield self.env.timeout(self.wait)
			print "Rider", self.name, "is done waiting, pressing the elevator"
