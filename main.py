#! /usr/bin/env python3
# coding: utf-8

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
    bad_guy = logic.logic.Badguy(game_map)
    mac_gyver = logic.logic.Mac(game_map, item_position)

    """generate graphic setting"""
    play = graphic.graphic.Game()
    play.run(game_map, mac_gyver, bad_guy, item_position)


if __name__ == "__main__":
    """execute main function of thie file if he is run like main program"""
    main()
