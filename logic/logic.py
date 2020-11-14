#! /usr/bin/env python3
# coding: utf-8
import pygame

class Map:
    """ there is one level but if we want other in futur, use a class for
        generate other map"""

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
        


class Mac(Character):

    def __init__(self):
        self.item = {"aiguille":False, "ether":False,"tube":False} 
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

    def __init__(self, random_position):
        self.position = random_position
