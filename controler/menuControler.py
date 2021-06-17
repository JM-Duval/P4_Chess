# -*-coding: utf-8 -*
# ! /usr/bin/env python
"""This file is a exercice about a program for help the chess tournament organization.
It is a first program with MVC structuring."""

import os
import sys

sys.path[:0] = ['../']
from model.menuModel import AllTournaments, StatisticsTournament, \
    AllPlayers
#from controler.tournamentControler import TournamentControler
from view.menuView import *


def statistics_menu_tournament(tournament_name):
    run = True
    while run:
        tournament = StatisticsTournament(tournament_name)
        display_statistics_tournament_menu(tournament_name)
        input = user_input(4)
        if input == '1':
            display_players(tournament.sorted_players_alpha())
        if input == '2':
            display_players(tournament.sorted_players_score())
        if input == '3':
            display_rounds(tournament.rounds())
        if input == '4':
            display_matchs(tournament.matchs())
        if input.upper() == 'Q':
            run = False

def list_tournaments_menu():
    tournaments = AllTournaments().list()
    run = True
    while run:
        display_list_tournaments(tournaments)
        input = user_input(len(tournaments))
        try:
            tournaments_selected = tournaments[int(input)-1]
            statistics_menu_tournament(tournaments_selected)
        except ValueError:
            run = False

def statistics_menu():
    run = True
    while run:
        display_statistics_menu()
        input = user_input(3)
        if input == '1':
            players_sorted_alpha = AllPlayers().sorted_alpha()
            display_players(players_sorted_alpha)
        if input == '2':
            players_sorted_elo = AllPlayers().sorted_elo()
            display_players(players_sorted_elo)
        if input == '3':
            list_tournaments_menu()
        if input.upper() == 'Q':
            run = False


def restart_tournament_menu():
    tournaments_open = AllTournaments().status_open()
    #display_list_tournaments(tournaments_open)
    run = True
    while run:
        display_list_tournaments(tournaments_open)
        input = user_input(len(tournaments_open))
        try:
            tournaments_selected = tournaments_open[int(input)-1]
            print(tournaments_selected)
            TournamentControler(tournaments_selected)
        except ValueError:
            run = False


def main_menu():
    while True:
        display_main_menu()
        input = user_input(4)
        if input == '1':
            print('menu 1')
        if input == '2':
            restart_tournament_menu()
        if input == '3':
            print('menu 3')
        if input == '4':
            statistics_menu()
        if input.upper() == 'Q':
            break


def select_players():
    players = AllPlayers().sorted_elo()
    display_players(players)
    display_title_select_players()
    selection = []
    while len(selection) < 8:
        input_user = input("")
        for player in selection:
            while players[int(input_user)-1] == player:
                display_selected_player_fail()
                input_user = input("")
        player_selected = players[int(input_user)-1]
        print(player_selected)
        selection.append(player_selected)
    display_players(selection)

#select_players()








"""

def list_all_tournaments():
    tournaments = AllTournaments().list()
    display_list_tournaments(tournaments)
    return tournaments

    try:
        tournament_selected = int(user_input(nb_tournaments))
        return tournaments[tournament_selected - 1]
    except ValueError:
        pass

def list_tournaments_open_menu_test():
    tournaments_open = AllTournaments().status_open()
    display_list_tournaments(tournaments_open)
    return tournaments_open
    try:
        tournament_selected = int(user_input(nb_tournaments))
        return tournaments[tournament_selected - 1]
    except ValueError:
        pass
"""
