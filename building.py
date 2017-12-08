import simpy
from Elevator import Elevator
from Rider import Rider
import sys
import pygame
import time
import random
import pygame
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
			elevator = image.load("elevator.bmp")
			elerect = elevator.get_rect()
			elerect.y = 500
			elerect.x = 100 * elevators.index(ele)
			ele.set_rect(elerect)
			ele.set_img(elevator)

	def run(self):
		while True:
			for event in self.event.get():
				if event.type == pygame.QUIT: sys.exit()
			black = 0, 0, 0
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
					print "STILL"+str(ele.curr_floor)+" pos:"+str((ele.rect.bottom-592)/5)
				elif ele.going_up:
					ele.rect = ele.rect.move([ele.speed[0],ele.speed[1]*-1])
					print "UP"+str(ele.curr_floor)+" pos:"+str((ele.rect.bottom-592)/5)
				elif not ele.going_up:
					ele.rect = ele.rect.move([ele.speed[0],ele.speed[1]])
					print "DOWN"+str(ele.curr_floor)+" pos:"+str((ele.rect.bottom-592)/5)
				if ele.rect.bottom > 600:
					print ("ERROR below"+str(ele.curr_floor)) * 10

				self.screen.blit(ele.img, ele.rect)
				print ele.name, "at", ele.curr_floor, "with stops", ele.stops, "and has riders",
				for rider in ele.riders:
					print rider.name,
				print ""
			for rider in self.riders:
				if not rider.request_elevator and not rider.chosen_elevator and rider.curr_floor != rider.desired_floor:
					#print "At", self.env.now, "Rider", rider.name, "is requesting the elevator "
					rider.request_elevator = True
					best = self.elevators[0]
					best_score = -10000
					for elevator in self.elevators:
						# ele_score = calculate(elevator)
						# wrong direction = -20 num_rider = -3
						ele_score = 0
						# print "CALCULATE = ", elevator.going_up, elevator.curr_floor <= rider.curr_floor, elevator.curr_floor < rider.desired_floor
						if ((elevator.going_up and elevator.curr_floor <= rider.curr_floor and elevator.curr_floor < rider.desired_floor) or
						(not elevator.going_up and elevator.curr_floor >= rider.curr_floor and elevator.curr_floor > rider.desired_floor)):
							ele_score+=20
						if len(elevator.stops):
							ele_score-=(len(elevator.riders)*4)
							# print "Correct direction adding 20"
						ele_score-=len(elevator.riders)*3
						# print elevator.name, "has ele_score of", ele_score
						if ele_score > best_score:
							# print "New ele_score added"
							best = elevator
							best_score = ele_score
					#print "Rider", rider.name, "is going in elevator", best.name
					best.add_stop(rider.curr_floor)
					rider.chosen_elevator = best
				elif rider.chosen_elevator and rider.curr_floor == rider.desired_floor:
					try:
						print "removing rider", rider.name,
						rider.chosen_elevator.riders.remove(rider)
						print "removal successful"
					except:
						print "failed removing rider",rider.name, rider.chosen_elevator.name, rider.chosen_elevator.riders
					try:
						rider.chosen_elevator.stops.remove(rider.curr_floor)
					except:
						print "failed removing stop"	
					rider.chosen_elevator = None

				print rider.name, "at", rider.curr_floor, rider.request_elevator, "wants to go to", rider.desired_floor, "with elevator", rider.chosen_elevator
					# elevator is choosen and picks up the next rider
			
			self.display.flip()
			yield self.env.timeout(1)
		# for Ele in Building:
		# 	print Ele.name
		# 	for rid in Ele.getRiders():
		# 		print rid.post()
