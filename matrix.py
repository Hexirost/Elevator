import random
import simpy
import panda3d
from Rider 		import Rider
from Elevator	import Elevator
from Building	import Building

RANDOM_SEED		 = 42
NUM_OF_ELEVATORS = 2
NUM_OF_RIDERS	 = 2

env = simpy.Environment()

elevators	= []
riders		= []
random.seed(RANDOM_SEED)

# Creating Elevators
for ele in range(NUM_OF_ELEVATORS):
	new_ele = Elevator("E-" + str(ele), env)
	elevators.append(new_ele)

# Creating Riders
for rid in range(NUM_OF_RIDERS):
	rider = Rider(chr(65+rid), env)
	riders.append(rider)

matrix = Building(elevators, riders,env)

for rider in riders:
	env.process(rider.run())
for elevator in elevators:
	env.process(elevator.run())
env.process(matrix.run())

env.run(until= 500)