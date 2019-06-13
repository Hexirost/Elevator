import random
import simpy
import pygame
from Rider 		import Rider
from Elevator	import Elevator
from Building	import Building

"""
This is the main run file. It creates an enviorment for simpy and then attaches that to each elevator and rider. 
Then starts up pygame. The elevator has sprites which are connected to pygame
"""

RANDOM_SEED		 = 42 #TODO Implement
NUM_OF_ELEVATORS = 10 #How many elevators
NUM_OF_RIDERS	 = 50 #How many Riders

env = simpy.RealtimeEnvironment(initial_time=0, factor=0.05, strict=False)

elevators	= []
riders		= []
random.seed(RANDOM_SEED)

pygame.init()

size = width, height = 1000, 800

screen	= pygame.display.set_mode(size)
display = pygame.display
image	= pygame.image
event	= pygame.event
# Creating Elevators
for ele in range(NUM_OF_ELEVATORS):
	new_ele = Elevator("E-" + str(ele), env)
	elevators.append(new_ele)

# Creating Riders
for rid in range(NUM_OF_RIDERS):
	rider = Rider(chr(65+rid), env)
	riders.append(rider)

matrix = Building(elevators, riders, env, screen, display, image, event)

for rider in riders:
	env.process(rider.run())
for elevator in elevators:
	env.process(elevator.run())
env.process(matrix.run())

#Length of runtime(In intervals but not accurate due to concurrency and speed of computer)
env.run(until= 500)