import simpy
from Elevator import Elevator
from Rider import Rider
import sys
import pygame
import time
import random

class Building():
	def __init__(self, elevators, riders, env, screen, display, image, event):
		self.elevators 	= elevators
		self.riders 	= riders
		self.env		= env
		self.screen		= screen
		self.display	= display
		self.image		= image
		self.event		= event

		for ele in elevators:
			elevator_img	= image.load("elevator.bmp")
			ele_rect		= elevator_img.get_rect()
			ele_rect.y		= 750
			ele_rect.x		= 100 * elevators.index(ele)
			ele.set_rect(ele_rect)
			ele.set_img(elevator_img)

		count=0
		for rider in riders:
			rider_img	= image.load("stick_"+str(count%4)+".bmp")
			rider_rect	= rider_img.get_rect()
			rider.rect	= rider_rect
			rider.img	= rider_img
			count+=1

	def run(self):
		while True:
			for event in self.event.get():
				if event.type == pygame.QUIT: sys.exit()
			black = 255, 255, 255
			self.screen.fill(black)
			for ele in self.elevators:
				for rider in self.riders:
					if rider.chosen_elevator == ele and ele.curr_floor == rider.curr_floor and rider.request_elevator:
						rider.request_elevator = False
						ele.add_rider(rider)
						ele.remove_stop(rider.curr_floor)
						ele.add_stop(rider.desired_floor)

				if ele.still:
					ele.rect = ele.rect.move([0,0])
				elif ele.going_up:
					ele.rect = ele.rect.move([ele.speed[0],ele.speed[1]*-1])
				elif not ele.going_up:
					ele.rect = ele.rect.move([ele.speed[0],ele.speed[1]])

				for rider in ele.riders:
					rider.rect.x = ele.rect.x
					rider.rect.y = ele.rect.y + 25

				self.screen.blit(ele.img, ele.rect)
				print(ele.name, "at", ele.curr_floor, "with stops", ele.stops, "and has riders",)
				for rider in ele.riders:
					print(rider.name,)
				print()
			for rider in self.riders:
				if not rider.request_elevator and not rider.chosen_elevator and rider.curr_floor != rider.desired_floor:
					rider.request_elevator = True
					best = self.elevators[0]
					best_score = -10000
					for elevator in self.elevators:
						ele_score = 0
						if ((elevator.going_up and elevator.curr_floor <= rider.curr_floor and elevator.curr_floor < rider.desired_floor) or
						(not elevator.going_up and elevator.curr_floor >= rider.curr_floor and elevator.curr_floor > rider.desired_floor)):
							ele_score+=200
						if len(elevator.stops):
							ele_score-=(len(elevator.stops)*4)
						ele_score-=abs(elevator.curr_floor-rider.desired_floor)
						if ele_score > best_score:
							best = elevator
							best_score = ele_score

					best.add_stop(rider.curr_floor)
					rider.chosen_elevator = best
					rider.rect.x = rider.chosen_elevator.rect.x

				elif rider.chosen_elevator and rider.curr_floor == rider.desired_floor:
					rider.chosen_elevator.riders.remove(rider)
					rider.chosen_elevator.stops.remove(rider.curr_floor)
					rider.chosen_elevator = None

				elif rider.chosen_elevator and rider.curr_floor != rider.desired_floor:# and rider.request_elevator :
					self.screen.blit(rider.img, rider.rect)
				print(rider.name, "at", rider.curr_floor, rider.request_elevator, "wants to go to", rider.desired_floor)
					# elevator is choosen and picks up the next rider
			self.display.flip()
			yield self.env.timeout(1)
