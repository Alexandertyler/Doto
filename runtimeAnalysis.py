#! /usr/bin/python

import tarrasque
import pylab as pl
import numpy as np



class Replay:
	
	def __init__(self):
		print("Initializing replay class.")
		#initialize players and their heros as objects
		self.playerPositions = dict()
		self.itemList = []

	def loadReplay(self, fileName):
		self.replay = tarrasque.StreamBinding.from_file(fileName)
		print("Replay fully parsed.")

	def initializeHeroDict(self):
		for player in self.replay.players:
			hero = player.hero
			heroName = hero.name
			initPosition = hero.position
			self.playerPositions[heroName] = [initPosition]
		for entry in self.playerPositions:
			print(entry)

	def timeStepAndLocation(self, stepSize):
		self.replay.go_to_tick(self.replay.tick + stepSize)
		for player in self.replay.players:
			hero = player.hero
			heroName = hero.name
			pos = hero.position
			self.playerPositions[heroName].append(pos)
		for entry in self.playerPositions:
			print(entry)

	def fullGameHeroLocations(self):
		for tick in replay.iter_ticks(start=game_start, end=game_end):
			break

	def playerMovementGraph(hero_name):
		for player in self.replay.players:
			if player.hero = hero_name:
				distance_data = []
				tick_data = []
				prevX, prevY = 0
				go_to_tick(game_start)
				currX, currY = player.hero.position
				#might have to change step size to get a better estimation of movement
				for tick in replay.iter_ticks(start=game_start, end=game_end):
					if not player.hero.is_alive:
						currX, currY = 0
						break
					prevX, prevY = currX, currY
					currX, currY = player.hero.location
					dist_traveled = manhattan(currX, currY, prevX, prevY)
					distance_data.append(dist_traveled)
					tick_data.append(tick)
				#call plotting function
				#plt.plot(tick_data, distance_data)
				#plt.show()
				#plt.savefig("./playerMovementGraph.png")

	def itemsPurchased(self):
		for player in self.replay.players:
			for item in player.hero.inventory:
				self.itemList.append((item, item.purchase_time))
		for item in self.itemList:
			print(item)

	def netGold(self):
		for player in self.replay.players:
			
				
class Heatmap:
	def __init__(self, x, y):
		self.x = x #An array of tuples of locations
		self.y = y

	def plot(self):
		#pl.subplot(121)
		pl.hexbin(self.x, self.y)
		pl.axis('image')
		pl.show()

def test():
	#replayClass = Replay() 
	#replayClass.loadReplay("test.dem")
	#replayClass.initializeHeroDict()
	#replayClass.timeStepAndLocation(1)
	#replayClass.itemsPurchased()
	x = [1, 1, 2, 2, 3, 4, 2, 2, 5]
	y = [1, 3, 2, 2, 4, 2, 1, 2, 3]
	heatmap = Heatmap(x, y)
	heatmap.plot()

def parse(command):
	if command == "q":
		exit(0)

	elif command == "h":
		print("q - quit\n intialize - Initialize a replay class\n loadReplay - Load a replay for analysis")

	elif command == "initialize":
		replayClass = Replay()

	elif command == "loadReplay":
		replayClass.loadReplay("test.dem")
	
	elif command == "initializeHeroDict":
		replayClass.initializeHeroDict()

	elif command == "test":
		test()	

	else:
		print("Command was not recognized. Enter -h for a list of commands.")
	

if __name__=='__main__':
	while True:
		command = raw_input("Please enter a command: ")
		parse(command)
