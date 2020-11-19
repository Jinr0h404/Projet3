#! /usr/bin/env python3
# coding: utf-8

import pygame
import random
import logic.logic
import graphic.graphic



"""generate obj map"""

test_map = logic.logic.Map()

"""generate all zone map with the file txt of the labyrinth"""
list_test_toto = test_map.test_area("data/level/laby.txt")

#print(list_test_toto)
#print(test_map.list_zone)
#print(test_map.list_floor)
#print("voilà pour le test")



"""generate character"""
#mac_gyver = logic.logic.Mac((0,0))
mac_gyver = logic.logic.Mac(test_map.list_start)
print(mac_gyver.position[0])
bad_guy = logic.logic.Mac(test_map.list_badguy)


#item
"""assign random position to an object"""
tube = logic.logic.Item()
aiguille = logic.logic.Item()
ether = logic.logic.Item()

ether_pos_px = ether.position_random(test_map.list_item)
tube_pos_px = tube.position_random(test_map.list_item)
aiguille_pos_px = aiguille.position_random(test_map.list_item)
print(ether.position)
print(ether_pos_px)



def main():

    graphic.graphic.playgame(test_map.list_start, test_map.list_finish, test_map.list_wall, test_map.list_floor, test_map.list_badguy, aiguille_pos_px, ether_pos_px, tube_pos_px)


if __name__ == "__main__":  #execute la fonction main de ce fichier si il est
    main()                  #lancer commer programme principal et non importé