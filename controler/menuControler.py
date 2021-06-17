# -*-coding: utf-8 -*
# ! /usr/bin/env python
"""This file is a exercice about a program for help the chess tournament organization.
It is a first program with MVC structuring."""

import os
import sys

sys.path[:0] = ['../']
from model.menuModel import AllTournaments, StatisticsTournament, \
    AllPlayers
from view.menuView import *


def list_all_tournaments():
    tournaments = AllTournaments().list()
    nb_tournaments = display_list_tournaments(tournaments)
    """
    try:
        tournament_selected = int(user_input(nb_tournaments))
        return tournaments[tournament_selected - 1]
    except ValueError:
        pass
    """

def list_tournaments_open():
    tournaments = AllTournaments().status_open()
    nb_tournaments = display_list_tournaments(tournaments)
    try:
        tournament_selected = int(user_input(nb_tournaments))
        return tournaments[tournament_selected - 1]
    except ValueError:
        pass


def run_statistics_tournament_menu():
    run = True
    while run:
        list_all_tournaments()
        input = user_input(2)

        display_statistics_tournament_menu()
        input = user_input(4)
        if input == '1':
            print('menu 1')
        if input == '2':
            print('menu 2')
        if input == '3':
            print('menu 3')
        if input == '4':
            print('menu 4')
        if input.upper() == 'Q':
            run = False


def run_statistics_menu():
    run = True
    while run:
        display_statistics_menu()
        input = user_input(3)
        if input == '1':
            players_sorted_alpha = AllPlayers().sorted_alpha()
            Display().players(players_sorted_alpha)
        if input == '2':
            players_sorted_elo = AllPlayers().sorted_elo()
            Display().players(players_sorted_elo)
        if input == '3':
            run_statistics_tournament_menu()
        if input.upper() == 'Q':
            run = False


def run_home_menu():
    while True:
        display_home_menu()
        input = user_input(4)
        if input == '1':
            print('menu 1')
        if input == '2':
            print('menu 2')
        if input == '3':
            print('menu 3')
        if input == '4':
            run_statistics_menu()
        if input.upper() == 'Q':
            break


run_home_menu()
