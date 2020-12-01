#! /usr/bin/env python3
# coding: utf-8

import pygame
import random
import logic.logic
import graphic.graphic





def main():
    """generate obj map"""
    game_map = logic.logic.Map()

    """generate all zone map with the file txt of the labyrinth"""
    game_map_position = game_map.area("data/level/laby.txt")


    """generate item"""
    item = logic.logic.Item(game_map.list_item)
    item_position = item.position_random

    """generate character"""
    bad_guy = logic.logic.Badguy(game_map.list_badguy)
    mac_gyver = logic.logic.Mac(game_map, item_position)
    print(game_map.list_floor)



    """generate graphic setting"""
    screen = graphic.graphic.Screen()
    play = graphic.graphic.Game()
    play.run(game_map, mac_gyver, bad_guy, item_position, screen)

if __name__ == "__main__":  #execute la fonction main de ce fichier si il est
    main()                  #lancer commer programme principal et non importé