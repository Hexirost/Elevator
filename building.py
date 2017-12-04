import simpy
import panda3d
from Elevator import Elevator
from Rider import Rider
import sys

class Building():
	def __init__(self, elevators, riders, env):
		self.elevators 	= elevators
		self.riders 	= riders
		self.env		= env

	def run(self):
		while True:
			for ele in self.elevators:
				for rider in self.riders:
					if rider.chosen_elevator == ele and ele.curr_floor == rider.curr_floor and rider.request_elevator:
						rider.request_elevator = False
						ele.add_rider(rider)
						ele.remove_stop(rider.curr_floor)
						ele.add_stop(rider.desired_floor)
						# Rider enters the elevator/elevator removes the current stop and adds rider desired stop
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
			yield self.env.timeout(1)
		# for Ele in Building:
		# 	print Ele.name
		# 	for rid in Ele.getRiders():
		# 		print rid.post()
