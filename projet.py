""" this project is a game. The goal is to move the character in a 15 / 15 
    square map and find the exit """

class Map:
    """ there is one level but if we want other in futur, use a class for
        generate other map"""
    AREA = []

    def __init__(self):
        self.position = {}

    def area(self, area):
        """# generate a list of dict where keys = position abs and ordo and 
        values the caracter in labyrinth file"""
        with open(area, "r") as map_file:
            zone = map_file.read().split()
            list_zone = []
            abs_map = 0
            ordo_map = 0
            for i in zone:
                for i in zone:
                    list_zone.append({(abs_map, ordo_map):zone[ordo_map][abs_map]})
                    abs_map += 1
                ordo_map += 1
                abs_map = 0
            return list_zone


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
list_map = test_map.area("laby.txt")
print(list_map)




"""test to assign random position to an object
in first we search each position is floor(not wall or start or finish)"""

test = list_map[1]
print(test)
print(test.values(), test.keys())
testCapt = test.keys()
print(testCapt)
test_values = test.values()
print(test_values)


list_possible_position = []
for i in list_map:
    dico = i
    for i in dico.values():
        if i == "O":
            list_possible_position.append(dico)
print(list_possible_position)

