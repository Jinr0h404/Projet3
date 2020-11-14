#! /usr/bin/env python3
# coding: utf-8

import pygame
import random
import logic.logic
import graphic.graphic



def main():
    pass





if __name__ == "__main__":  #execute la fonction main de ce fichier si il est
    main()                  #lancer commer programme principal et non importé


"""generate map with the file txt of the labyrinth"""

test_map = logic.logic.Map()
list_map = test_map.area("data/level/laby.txt")


"""generate character"""
# mac_gyver = logic.logic.Mac("MacGyver", list_start_position_px)


"""test to assign random position to an object
in first we search each position is floor(not wall or start or finish)"""



list_possible_position = []
list_wall_position = []
list_floor_position = []
list_start_position = []
list_finish_position = []
bad_guy_position = []

for i in list_map:       # pour chaque element de ma liste de dictionnaire
    dico = i
    print(dico)
    for i in dico.values(): # je recupere la valeur de mon dico
        print(i)
        if i == "O":
            list_possible_position.append(dico) # si valeur == O alors j'ajoute le dico a la liste possible
            for key in dico.keys():
                list_floor_position.append(key)   # et je met la clef du dico donc sa position dans la liste des positions de sol
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


"""ici je vais convertir mes listes de position sol et mur en coordonnée de pixel"""
list_wall_position_px = []
list_floor_position_px = []
list_start_position_px = []
list_finish_position_px = []
bad_guy_position_px = []
# comme je suis parti sur des surface de 45px pour mes tuiles, je multiplie mes abs et mes ordo par 45
for element in list_wall_position:
    list_wall_position_px.append((element[0]*45, element[1] * 45))
for element in list_floor_position:
    list_floor_position_px.append((element[0]*45, element[1] * 45))
for element in list_start_position:
    list_start_position_px.append((element[0]*45, element[1] * 45))
for element in list_finish_position:
    list_finish_position_px.append((element[0]*45, element[1] * 45))
for element in bad_guy_position:
    bad_guy_position_px.append((element[0]*45, element[1] * 45))

graphic.graphic.playgame(list_start_position_px, list_finish_position_px, list_wall_position_px, list_floor_position_px, bad_guy_position_px)