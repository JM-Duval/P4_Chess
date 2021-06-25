# -*-coding: utf-8 -*
#! /usr/bin/env python
"""This file is a exercice about a program for help the chess tournament organization.
It is a first program with MVC structuring."""

import os
import sys
sys.path[:0]=['../']
from pathlib import Path
from tinydb import TinyDB, Query, where
from model.dataBasePlayersModel import DataBasePlayers
from model.dataBaseTournamentModel import DataTournament


"""
class AllPlayers:
    def __init__(self):
        self.players = DataBasePlayers()

    def sorted_alpha(self):
        return [players for players in self.players.sorted_alpha()]

    def sorted_elo(self):
        players = []
        for player in self.players.sorted_elo():
            players.append(player)
        return players
        #return [players.append(player) for player in self.players.sorted_elo()]


    def test(self): # OK
        for i in self.sorted_alpha():
            print(i)
        for i in self.sorted_elo():
            print(i)


class StatisticsTournament:
    def __init__(self, tournament_name):
        self.tournament_name = tournament_name
        self.tournament = DataTournament(self.tournament_name)

    def sorted_players_alpha(self):
        return [player for player in self.tournament.sorted_alpha()]

    def sorted_players_score(self):
        return [player for player in self.tournament.sorted_score()]

    def rounds(self):
        return [self.tournament.load_tournament().rounds[i].round_name
                for i in range(len(self.tournament.load_tournament().rounds))]

    def matchs(self):
        matchs = []
        for round in self.tournament.load_tournament().rounds:
            [matchs.append(players) for players in round.matchs]
        return matchs

    def test(self): # OK
        print('\ntest sorted_players_alpha\n')
        for i in self.sorted_players_alpha():
            print(i)
        print('\ntest sorted_players_score\n')
        for i in self.sorted_players_score():
            print(i)
        print('\ntest_rounds\n')
        for i in self.rounds():
            print(i)
        print('\ntest_matchs\n')
        for i in self.matchs():
            print(i)

#StatisticsTournament('Word_tour_Moto_GP').test()

class AllTournaments:
    def __init__(self):
        self.name_table = 'tournament'
        self.name_file = 'tournaments.json'
        origin_path = (sys.path[(len(sys.path)) - 2][:-4])
        path_data_tournament = os.path.join(origin_path, 'data/tournaments')
        db = TinyDB(os.path.join(path_data_tournament, self.name_file))
        self.tournament_table = db.table(self.name_table)

    def list(self):
        list_tournaments = []
        [list_tournaments.append(tour['tournament_name']) for tour in
         self.tournament_table.all()]
        return list_tournaments

    def status_open(self):
        list_tournaments_open = []
        for tour in self.tournament_table.all():
            if tour['status'] == 'open':
                list_tournaments_open.append(tour['tournament_name'])
        return list_tournaments_open

    def status_close(self):
        list_tournaments_closed = []
        for tour in self.tournament_table.all():
            if tour['status'] == 'close':
                list_tournaments_closed.append(tour)
        return list_tournaments_closed

    def test(self): #ok
        print('\ntest\n')
        #print(self.list())
        print(self.status_open())
        print(self.status_close())

"""

#AllTournaments().test()
