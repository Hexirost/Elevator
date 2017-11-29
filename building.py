import simpy
import panda3d
from Elevator import Elevator
from Rider import Rider
import random

RANDOM_SEED		 = 42
NUM_OF_ELEVATORS = 2
NUM_OF_RIDERS	 = 5

Building = []
Riders = []

env = simpy.Environment()

for ele in range(NUM_OF_ELEVATORS):
	new_ele = Elevator("Elevator "+str(ele))
	Building.append(new_ele)

for rid in range(NUM_OF_RIDERS):
	rider = Rider(chr(65+rid), env)
	Riders.append(rider)
	random.choice(Building).addRider(rider)		# TODO: REMOVE

# for Ele in Building:
# 	print Ele.name
# 	for rid in Ele.getRiders():
# 		print rid.post()

for rider in Riders:
	env.process(rider.run())
env.run(until= 5)