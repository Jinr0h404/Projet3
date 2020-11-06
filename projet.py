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


class Character:
    """ Character class allow to create obj character with position attribute
    and move method"""
    def __init__(self, name, first_position):
        self.name = name
        self.position = first_position
        self.item = {"aiguille":"False", "ether":"False","tube":"False"} 
        # move methode check if sprite is with an item, if yes, change
        # value of dict "item" to true with item key
        # for the last move if all item value != True, it's lost

    def move_up(self):
#self.position = self.position[1] += 1 if position define by list of 2 item abs and ordo
        pass

    def move_down(self, input_key):
        pass

    def move_left(self, input_key):
        pass

    def move_right(self, input_key):
        pass



test_map = Map()
print(test_map.area("laby.txt"))
list_map = test_map.area("laby.txt").split()
print(list_map)
list_position_on_map = []
print(list_map[0][0])
testDic = list_map[0][0]
list_position_on_map = [{list_map[0][0]:testDic}]
print(list_position_on_map)