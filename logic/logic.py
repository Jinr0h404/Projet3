#! /usr/bin/env python3
# coding: utf-8
import pygame
import random

class Map:
    """ there is one level but if we want other in futur, use a class for
        generate other map"""

    def __init__(self):
        self.list_zone = []
        self._pos_floor = []
        self.sprite_size = 45

    def area(self, area):
        """# generate a list of dict where keys = position abs and ordo and 
        values the caracter in labyrinth file"""
        with open(area, "r") as map_file:
            zone = map_file.read().split()
            list_zone = []
            abs_map = 0
            ordo_map = 0
            # add each element of the file in the list and convert directly abs and ordo in sprite size 45px
            for i in zone:
                for i in zone:
                    list_zone.append({(abs_map*self.sprite_size, ordo_map*self.sprite_size):zone[ordo_map][abs_map]})
                    abs_map += 1
                ordo_map += 1
                abs_map = 0
            return list_zone

    def test_area(self, area):
        """# generate a list of dict where keys = position abs and ordo and 
        values the caracter in labyrinth file"""
        with open(area, "r") as map_file:
            zone = map_file.read().split()
            list_zone = []
            abs_map = 0
            ordo_map = 0
            # add each element of the file in the list and convert directly abs and ordo in sprite size 45px
            for i in zone:
                for i in zone:
                    list_zone.append({(abs_map*self.sprite_size, ordo_map*self.sprite_size):zone[ordo_map][abs_map]})
                    abs_map += 1
                ordo_map += 1
                abs_map = 0
            self.list_zone = list_zone
            return list_zone

    @property
    def list_floor(self):
        list_floor_positionTest = []
        for i in self.list_zone:       # pour chaque element de ma liste de dictionnaire
            dico = i
            print(dico)
            for i in dico.values(): # je recupere la valeur de mon dico
                print(i)
                if i == "O":
                    for key in dico.keys():
                        list_floor_positionTest.append(key)   # et je met la clef du dico donc sa position dans la liste des positions de sol
                        #list_possible_position.append(key)
        self._pos_floor = list_floor_positionTest
        return self._pos_floor
    


class Character:
    """ Character class allow to create obj character with position attribute
    and move method"""
    def __init__(self, name, position):
        self.name = name
        self.position = position
        


class Mac(Character):

    def __init__(self, position):
        self.item = {"aiguille":False, "ether":False,"tube":False} 
        Character.__init__(self, "MacGyver", position)
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


class Badguy(Character):

    def __init__(self):
        pass

class Item:

    def __init__(self):
        self.position = ()

    """generate item with random position"""
    def position_random(self, list_possible_position):
        position_random = random.choice(list_possible_position)
        return position_random