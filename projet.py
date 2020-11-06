""" this project is a game. The goal is to move the character in a 15 / 15 
	square map and find the exit """

class Map:
	""" there is one level but if we want other in futur, use a class for
		generate other map"""
	AREA = []

	def __init__(self):
		self.position = {}

	def area(self, area):
		with open(area, "r") as map_file:
			zone = map_file.read()
			return zone
			
test_map = Map()
print(test_map.area("laby.txt"))
