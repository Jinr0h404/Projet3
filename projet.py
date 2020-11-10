import pygame

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
list_map = test_map.area("data/level/laby.txt")
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
list_wall_position = []
list_floor_position = []
for i in list_map:       # pour chaque element de ma liste de dictionnaire
    dico = i
    print(dico)
    for i in dico.values(): # je recupere la valeur de mon dico
        print(i)
        if i == "O":
            list_possible_position.append(dico) # si valeur == O alors j'ajoute le dico a la liste possible
            for key in dico.keys():
                list_floor_position.append(key)   # et je met la clef du dico donc sa position dans la liste des positions de sol
        else:
            for key in dico.keys():
                list_wall_position.append(key)  # et je mets le reste des clefs donc les positions de murs, dans la liste des positions de mur
print(list_possible_position)
print(list_wall_position)
print(list_floor_position)


"""ici je vais convertir mes listes de position sol et mur en coordonnée de pixel"""





"""ici je teste la partie pygame avant de tout separer en module"""

pygame.init()

ecran = pygame.display.set_mode((675, 675))
pygame.display.set_caption("Help MacGyver")
picture_menu = pygame.image.load("data/projet_3.png").convert_alpha()
pygame.display.set_icon(picture_menu)


noir = (10, 10, 10)

picture_macgy = pygame.image.load("data/MacGyver.png").convert_alpha() # cherche et tranforme l'image en surface puis la converti
picture_floor = pygame.image.load("data/floor15.png").convert_alpha()
picture_wall = pygame.image.load("data/wall15.png").convert_alpha()

rect_macgy = picture_macgy.get_rect()
rect_floor = picture_floor.get_rect()
rect_wall = picture_wall.get_rect()



list_wall = [(10, 10),(30, 30), (50,50), (90,90), (120,120), (150, 150)]

continuer = True

while continuer: 
    ecran.fill(noir) # definit une couleur de fond pour l'ecran
    for element in list_wall:
        ecran.blit(picture_floor, (element))
    for element in list_wall_position:
        ecran.blit(picture_wall, element)
    for element in list_floor_position:
        ecran.blit(picture_floor, element)
    ecran.blit(picture_floor, list_wall[2]) # blit copie l'image_surface en parametre sur la surface de l'ecran
    ecran.blit(picture_macgy, (0, 0, 20, 20)) # le tuple 0,0 donne la position de départ de l'image
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer = False
    pygame.display.flip() # dit à pygame d'afficher la surface du jeu

pygame.quit()