#! /usr/bin/env python3
# coding: utf-8
import pygame
import random

class Map:
    """ there is one level but if we want other in futur, use a class for
        generate other map"""

    def __init__(self):
        self.list_zone = []
        self._list_item = []
        self._pos_floor = []
        self._pos_wall = []
        self._pos_finish = []
        self._pos_start = []
        self._pos_badguy = []
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

    """method to assign position to an object in first we search each position is floor(all except wall)"""
    @property
    def list_floor(self):
        list_floor_positionTest = []
        for i in self.list_zone:       # pour chaque element de ma liste de dictionnaire
            dico = i
            #print(dico)
            for i in dico.values(): # je recupere la valeur de mon dico
                #print(i)
                if i != "X":
                    for key in dico.keys():
                        list_floor_positionTest.append(key)   # et je met la clef du dico donc sa position dans la liste des positions de sol
                        #list_possible_position.append(key)
        self._pos_floor = list_floor_positionTest
        return self._pos_floor
    
    @property
    def list_wall(self):
        list_wall_positionTest = []
        for i in self.list_zone:       # pour chaque element de ma liste de dictionnaire
            dico = i
            for i in dico.values(): # je recupere la valeur de mon dico
                if i == "X":
                    for key in dico.keys():
                        list_wall_positionTest.append(key)   # et je met la clef du dico donc sa position dans la liste des positions de sol
                        #list_possible_position.append(key)
        self._pos_wall = list_wall_positionTest
        return self._pos_wall

    @property
    def list_start(self):
        list_start_positionTest = []
        for i in self.list_zone:       # pour chaque element de ma liste de dictionnaire
            dico = i
            for i in dico.values(): # je recupere la valeur de mon dico
                if i == "D":
                    for key in dico.keys():
                        list_start_positionTest.append(key)   # et je met la clef du dico donc sa position dans la liste des positions de sol
                        #list_possible_position.append(key)
        self._pos_start = list_start_positionTest
        return self._pos_start

    @property
    def list_finish(self):
        list_finish_positionTest = []
        for i in self.list_zone:       # pour chaque element de ma liste de dictionnaire
            dico = i
            for i in dico.values(): # je recupere la valeur de mon dico
                if i == "A":
                    for key in dico.keys():
                        list_finish_positionTest.append(key)   # et je met la clef du dico donc sa position dans la liste des positions de sol
                        #list_possible_position.append(key)
        self._pos_finish = list_finish_positionTest
        return self._pos_finish

    @property
    def list_badguy(self):
        list_badguy_positionTest = []
        for i in self.list_zone:       # pour chaque element de ma liste de dictionnaire
            dico = i
            for i in dico.values(): # je recupere la valeur de mon dico
                if i == "B":
                    for key in dico.keys():
                        list_badguy_positionTest.append(key)   # et je met la clef du dico donc sa position dans la liste des positions de sol
                        #list_possible_position.append(key)
        self._pos_badguy = list_badguy_positionTest
        return self._pos_badguy

    """method to assign position to an object in first we search each position is possible(not wall or start or finish or badguy pos)"""
    @property
    def list_item(self):
        list_item_positionTest = []
        for i in self.list_zone:       # pour chaque element de ma liste de dictionnaire
            dico = i
            #print(dico)
            for i in dico.values(): # je recupere la valeur de mon dico
                #print(i)
                if i == "O":
                    for key in dico.keys():
                        list_item_positionTest.append(key)   # et je met la clef du dico donc sa position dans la liste des positions de sol
                        #list_possible_position.append(key)
        self._pos_item = list_item_positionTest
        return self._pos_item


class Character:
    """ Character class allow to create obj character with position attribute
    and move method"""
    def __init__(self, name, position):
        self.name = name
        self.position = position
        


class Mac(Character):

    def __init__(self, position, floor):
        self.item = {"aiguille":False, "ether":False,"tube":False}
        self.list_move = floor 
        Character.__init__(self, "MacGyver", position)
        # move methode check if sprite is with an item, if yes, change
        # value of dict "item" to true with item key
        # for the last move if all item value != True, it's lost

    def move_up(self):
        # position list for mac have just 1 element, tuple. change valeur of Y
        possible_move = self.list_move
        if (self.position[0][0], self.position[0][1] - 45) in possible_move:
            print("yes")
        else:
            print("nop y'a pas")
        self.position = [(self.position[0][0], self.position[0][1] - 45)] #if position define by list of 2 item abs and ordo
        return self.position

    def move_down(self):
        self.position = [(self.position[0][0], self.position[0][1] + 45)]
        return self.position

    def move_left(self):
        self.position = [(self.position[0][0] - 45, self.position[0][1])] 
        return self.position

    def move_right(self):
        wanted_move = (self.position[0][0] + 45, self.position[0][1])
        possible_move = self.list_move
        if wanted_move in possible_move:
            self.position = [wanted_move]
        else:
            print("si seulement j'avais mon couteau pour percer ce mur") 
        return self.position


class Badguy(Character):

    def __init__(self, position):
        Character.__init__(self, "BadGuy", position)


class Item:

    def __init__(self):
        self.position = ()

    """generate item with random position"""
    def position_random(self, list_possible_position):
        position_random = random.choice(list_possible_position)
        return position_random