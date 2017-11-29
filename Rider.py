import random

class Rider():

	def __init__(self, name):
		self.wait  = random.randint(0,5)
		self.level = 0
		self.dest  = random.randint(0,10) 
		self.name  = name 

	def post(self):
		return ("Hello my name is " + str(self.name))
