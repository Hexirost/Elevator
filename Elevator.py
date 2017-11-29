import simpy
import panda3d

MAX_EVELVATOR_SIZE = 5

class Elevator():

	def __init__(self, name):
		self.max 	= MAX_EVELVATOR_SIZE
		self.called = False 
		self.riders = []
		self.name 	= name

	def addRider(self,rider):
		self.riders.append(rider)

	def getRiders(self):
		return self.riders


