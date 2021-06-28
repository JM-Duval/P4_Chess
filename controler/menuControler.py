# -*-coding: utf-8 -*
# ! /usr/bin/env python
"""This file is a exercice about a program for help the chess tournament organization.
It is a first program with MVC structuring."""

from controler.tournamentControler import run_tournament
from controler.inputUserControler import UserInput
from controler.dataBasePlayersControler import enter_new_player, del_player, edit_player
from model.dataBaseTournamentModel import DataTournament, AllTournaments
from model.dataBasePlayersModel import DataBasePlayers
from view.menuView import DisplayMenu, DisplayMessage, DisplayList
import os
import sys
sys.path[:0] = ['../']

user_input = UserInput().interval


def statistics_tournament_menu(tournament_name):
    run = True
    while run:
        tournament = DataTournament(tournament_name)
        DisplayMenu().statistics_tournament(tournament_name)
        input = user_input(5)
        if input == '1':
            DisplayList().infos_tour(tournament.get_infos_tour())
        if input == '2':
            DisplayList().players(tournament.get_sorted_players_alpha())
        if input == '3':
            DisplayList().score_players(tournament.get_sorted_players_score())
        if input == '4':
            DisplayList().rounds(tournament.get_rounds())
        if input == '5':
            DisplayList().matchs(tournament.get_matchs())
        if input.upper() == 'Q':
            run = False


def list_tournaments_menu():
    tournaments = AllTournaments().list()
    run = True
    while run:
        os.system('clear')
        DisplayList().tournaments(tournaments)
        input = user_input(len(tournaments))
        try:
            tournaments_selected = tournaments[int(input)-1]
            statistics_tournament_menu(tournaments_selected)
            break
        except ValueError:
            run = False


def statistics_menu():
    run = True
    while run:
        DisplayMenu().statistics()
        input = user_input(3)
        if input == '1':
            players_sorted_alpha = DataBasePlayers().sorted_alpha()
            DisplayList().players(players_sorted_alpha)
        if input == '2':
            players_sorted_elo = DataBasePlayers().sorted_elo()
            DisplayList().players(players_sorted_elo)
        if input == '3':
            list_tournaments_menu()
        if input.upper() == 'Q':
            run = False


def statistics_players_menu():
    run = True
    while run:
        DisplayMenu().statistics_players()
        input = user_input(4)
        if input == '1':
            players = DataBasePlayers().load()
            DisplayList().players(players)
        if input == '2':
            infos_player = UserInput().infos_player()
            enter_new_player(infos_player)
        if input == '3':
            edit_player()
        if input == '4':
            players = DataBasePlayers().load()
            DisplayList().players(players)
            input = user_input(len(players))
            del_player(players[int(input)-1])
        if input.upper() == 'Q':
            run = False


class LaunchTournamentMenu:
    def __init__(self):
        pass

    def go_start_new_tournament(self):
        os.system('clear')
        while True:
            players_for_tour = self.select_players()
            if players_for_tour is False:
                break
            else:
                run_tournament(None, players_for_tour)
                break

    def select_players(self):
        selection = []
        try:
            while len(selection) < 8:
                os.system('clear')
                DisplayMessage().list_players()
                players = DataBasePlayers().sorted_elo()
                DisplayList().players(players)
                input_user = user_input(len(players))
                player_selected = players[int(input_user) - 1]
                while player_selected in selection:
                    DisplayMessage().player_error(player_selected)
                    input_user = user_input(len(players))
                    player_selected = players[int(input_user) - 1]
                selection.append(player_selected)
                DisplayMessage().selected_players()
                DisplayList().players(selection)
            return selection
        except ValueError:
            return False

    def go_restart_tournament(self):
        os.system('clear')
        tournament = self.select_tournament()
        while True:
            if tournament is False:
                break
            else:
                run_tournament(tournament, None)
                break

    def select_tournament(self):
        tournaments_open = AllTournaments().status_open()
        try:
            if len(tournaments_open) == 0:
                DisplayMessage().no_tournament()
                return False
            else:
                DisplayList().tournaments(tournaments_open)
                input = user_input(len(tournaments_open))
                tournaments_selected = tournaments_open[int(input) - 1]
                return tournaments_selected
        except ValueError:
            return False


def main_menu():
    while True:
        DisplayMenu().main()
        input = user_input(4)
        if input == '1':
            LaunchTournamentMenu().go_start_new_tournament()
        if input == '2':
            LaunchTournamentMenu().go_restart_tournament()
        if input == '3':
            statistics_players_menu()
        if input == '4':
            statistics_menu()
        if input.upper() == 'Q':
            break





