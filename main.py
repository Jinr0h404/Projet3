#! /usr/bin/env python3
# coding: utf-8

import pygame
import random
import logic.logic
import graphic.graphic



"""generate map with the file txt of the labyrinth"""

test_map = logic.logic.Map()
list_map = test_map.area("data/level/laby.txt")



"""test to assign random position to an object
in first we search each position is floor(not wall or start or finish)"""



list_possible_position_old = []
list_possible_position = []
list_wall_position = []
list_floor_position = []
list_start_position = []
list_finish_position = []
bad_guy_position = []
#list_test_toto = test_map.area("data/level/laby.txt").list_floor(list_map)
#print(list_test_toto)

for i in list_map:       # pour chaque element de ma liste de dictionnaire
    dico = i
    print(dico)
    for i in dico.values(): # je recupere la valeur de mon dico
        print(i)
        if i == "O":
            list_possible_position_old.append(dico) # si valeur == O alors j'ajoute le dico a la liste possible
            for key in dico.keys():
                list_floor_position.append(key)   # et je met la clef du dico donc sa position dans la liste des positions de sol
                list_possible_position.append(key)
        elif i =="D":
            for key in dico.keys():
                list_start_position.append(key)
        elif i == "A":
            for key in dico.keys():
                list_finish_position.append(key)
        elif i == "B":
            for key in dico.keys():
                bad_guy_position.append(key)
                list_floor_position.append(key)
        else:
            for key in dico.keys():
                list_wall_position.append(key)  # et je mets le reste des clefs donc les positions de murs, dans la liste des positions de mur


"""generate character"""
mac_gyver = logic.logic.Mac((0,0))
#bad_guy = logic.logic.Mac("BadGuy", bad_guy_position_px)


#item
tube = logic.logic.Item()
aiguille = logic.logic.Item()
ether = logic.logic.Item()
#item = [tube.position, aiguille.position, ether.position]
ether_pos_px = ether.position_random(list_possible_position)
tube_pos_px = tube.position_random(list_possible_position)
aiguille_pos_px = aiguille.position_random(list_possible_position)
print(tube.position)
print(aiguille.position)
print(ether.position)
#print(item)
print(ether_pos_px)

graphic.graphic.playgame(list_start_position, list_finish_position, list_wall_position, list_floor_position, bad_guy_position, aiguille_pos_px, ether_pos_px, tube_pos_px)




def main():
    pass



if __name__ == "__main__":  #execute la fonction main de ce fichier si il est
    main()                  #lancer commer programme principal et non importé