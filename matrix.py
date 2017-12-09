import random
import simpy
import panda3d
import pygame
from Rider 		import Rider
from Elevator	import Elevator
from Building	import Building

RANDOM_SEED		 = 42
NUM_OF_ELEVATORS = 10
NUM_OF_RIDERS	 = 50

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

env.run(until= 10000)