#! /usr/bin/env python3
# coding: utf-8

import random


class Map:
    """there is one level but if we want other in futur, use this class for
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
        """ generate a list of dict where keys = position abs and ordo and
        values the caracter in labyrinth file.txt. this method convert each
        line in the file.txt. with loop converts each line of the file to
        an item in a list. each item of the list has an y axes position and
        each element of the item has an x axes position """
        with open(area, "r") as map_file:
            zone = map_file.read().split()
            list_zone = []
            abs_map = 0
            ordo_map = 0
            # add each element of the file in the list and convert
            # directly abs and ordo in sprite size 45px
            for i in zone:
                for i in zone:
                    list_zone.append(
                        {
                            (
                                abs_map * self.sprite_size,
                                ordo_map * self.sprite_size,
                            ): zone[ordo_map][abs_map]
                        }
                    )
                    abs_map += 1
                ordo_map += 1
                abs_map = 0
            self.list_zone = list_zone
            return list_zone

    @property
    def list_floor(self):
        """method to define a list of position according to the character in
        the labyrinth file. first search each position on the ground (all
        except the wall)"""
        list_floor_position = []
        for i in self.list_zone:  # for each element in my dict list
            dico = i
            for i in dico.values():  # recover value of my dict
                if i != "X":
                    for key in dico.keys():
                        list_floor_position.append(
                            key
                        )  # put the key = position in the list of floor tile
        self._pos_floor = list_floor_position
        return self._pos_floor

    @property
    def list_wall(self):
        list_wall_position = []
        for i in self.list_zone:
            dico = i
            for i in dico.values():
                if i == "X":
                    for key in dico.keys():
                        list_wall_position.append(
                            key
                        )
        self._pos_wall = list_wall_position
        return self._pos_wall

    @property
    def list_start(self):
        list_start_position = []
        for i in self.list_zone:
            dico = i
            for i in dico.values():
                if i == "D":
                    for key in dico.keys():
                        list_start_position.append(
                            key
                        )
        self._pos_start = list_start_position
        return self._pos_start

    @property
    def list_finish(self):
        list_finish_position = []
        for i in self.list_zone:
            dico = i
            for i in dico.values():
                if i == "A":
                    for key in dico.keys():
                        list_finish_position.append(
                            key
                        )
        self._pos_finish = list_finish_position
        return self._pos_finish

    @property
    def list_badguy(self):
        list_badguy_position = []
        for i in self.list_zone:
            dico = i
            for i in dico.values():
                if i == "B":
                    for key in dico.keys():
                        list_badguy_position.append(
                            key
                        )
        self._pos_badguy = list_badguy_position
        return self._pos_badguy

    @property
    def list_item(self):
        """method to define list of possible position for an object in first
        we search each position is possible(not wall or start or finish or
        badguy pos)"""
        list_item_position = []
        for i in self.list_zone:
            dico = i
            for i in dico.values():
                if i == "O":
                    for key in dico.keys():
                        list_item_position.append(
                            key
                        )
        self._pos_item = list_item_position
        return self._pos_item


class Character:
    """Character class allow to create obj character with position attribute
    and move method"""

    def __init__(self, name, position):
        self.name = name
        self.position = position


class Mac(Character):
    def __init__(self, position, item_pos):
        self.item = {"aiguille": False, "ether": False, "tube": False}
        self.list_move = position.list_floor
        self.safe = False
        self.item_pos = item_pos
        self.enemy = position.list_badguy
        self.finish_pos = position.list_finish
        self.free = False
        Character.__init__(self, "MacGyver", position.list_start)
        # move methode check if sprite is with an item, if yes, change
        # value of dict "item" to true with item key
        # for the last move if all item value != True, it's lost

    def move_up(self):
        # position list for mac have just 1 element, tuple. change valeur of Y
        wanted_move = (self.position[0][0], self.position[0][1] - 45)
        possible_move = self.list_move
        if wanted_move in possible_move:
            if wanted_move == self.enemy[0]:
                if self.safe is False:
                    print("go start")
                else:
                    print("bingo")
            self.position = [
                wanted_move
            ]  # if position define by list of 2 item abs and ordo
            for key, value in self.item_pos.items():
                if value == self.position[0]:
                    self.item[key] = True
            if all(value is True for value in self.item.values()):
                self.safe = True
            if self.position == self.finish_pos and self.safe is True:
                self.free = True
        return self.position

    def move_down(self):
        wanted_move = (self.position[0][0], self.position[0][1] + 45)
        possible_move = self.list_move
        if wanted_move in possible_move:
            if wanted_move == self.enemy[0]:
                if self.safe is False:
                    print("go start")
                else:
                    print("bingo")
            self.position = [wanted_move]
            for key, value in self.item_pos.items():
                if value == self.position[0]:
                    self.item[key] = True
            if all(value is True for value in self.item.values()):
                self.safe = True
        if self.position == self.finish_pos and self.safe is True:
            self.free = True
        return self.position

    def move_left(self):
        wanted_move = (self.position[0][0] - 45, self.position[0][1])
        possible_move = self.list_move
        if wanted_move in possible_move:
            if wanted_move == self.enemy[0]:
                if self.safe is False:
                    print("go start")
                else:
                    print("bingo")
            self.position = [wanted_move]
            for key, value in self.item_pos.items():
                if value == self.position[0]:
                    self.item[key] = True
            if all(value is True for value in self.item.values()):
                self.safe = True
            if self.position == self.finish_pos and self.safe is True:
                self.free = True
        return self.position

    def move_right(self):
        wanted_move = (self.position[0][0] + 45, self.position[0][1])
        possible_move = self.list_move
        if wanted_move in possible_move:
            if wanted_move == self.enemy[0]:
                if self.safe is False:
                    print("go start")
                else:
                    print("bingo")
            self.position = [wanted_move]
            for key, value in self.item_pos.items():
                if value == self.position[0]:
                    self.item[key] = True
                    print(self.item)
            if all(value is True for value in self.item.values()):
                self.safe = True
        if self.position == self.finish_pos and self.safe is True:
            self.free = True
        return self.position


class Badguy(Character):
    def __init__(self, position):
        self.list_move = position.list_floor
        self._field_view = []
        Character.__init__(self, "BadGuy", position.list_badguy)

    @property
    def field_of_view(self):
        keep_move = [
            (self.position[0][0] + 45, self.position[0][1]),
            (self.position[0][0] - 45, self.position[0][1]),
            (self.position[0][0], self.position[0][1] + 45),
            (self.position[0][0], self.position[0][1] - 45),
        ]
        possible_move = self.list_move
        for element in keep_move:
            if element in possible_move:
                self._field_view.append(element)
        return self._field_view


class Item:
    def __init__(self, list_possible_position):
        self.position = list_possible_position
        self._position_item = []

    """generate item with random position"""

    @property
    def position_random(self):
        position_random = random.sample(self.position, 3)
        liste_pos_item = {
            "ether": position_random[0],
            "aiguille": position_random[1],
            "tube": position_random[2],
        }
        self._position_item = liste_pos_item
        return self._position_item
