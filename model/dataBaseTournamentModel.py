# -*-coding: utf-8 -*
#! /usr/bin/env python
"""This file is a exercice about tinydb.
Web_site_link = https://www.docstring.fr/blog/tinydb-une-base-de-donnees-adaptee-vos-projets/"""

from tinydb import TinyDB, Query, where
import sys
sys.path[:0]=['../']
#from controler.tournamentControler import TournamentControler
from model.player import *
# TinyDB is the database
# Query allows to query the data base
# where allows to refine the search

class DataTournament:
    def __init__(self, tournament_name, location, start_time, tour_number, time_control):
        self.tournament_name = tournament_name
        self.location = location
        self.start_time = start_time
        self.tour_number = tour_number
        self.time_control = time_control
        self.name_table = "data_tournament"
        self.name_file = self.tournament_name+'.json'
        db = TinyDB(self.name_file)
        self.tournament_table = db.table(self.name_table)

    def record(self):
        self.tournament_table.insert({'tournament_name': self.tournament_name,
                                      'start_time': self.start_time,
                                      'tour_number' : self.tour_number,
                                      'location': self.location,
                                      'time_control': self.time_control})

    def insert(self, data_tournament):
        self.tournament_table.insert(data_tournament)

    def search(self, player):
        pass


class DataTournamentPlayers:
    def __init__(self, tournament_name, round_name):
        self.tournament_name = tournament_name
        self.name_table = round_name
        self.name_file = self.tournament_name+'.json'
        db = TinyDB(self.name_file)
        self.players_table = db.table(self.name_table)

    def search(self, player):
        Person = Query()
        if self.players_table.search(Person.last_name == player):
            return True
        else:
            return False

    def _serialized(self, player):
        serialized_player = {
        'first_name' : player.first_name,
        'last_name' : player.last_name,
        'date_birth' : player.date_birth,
        'sexe' : player.sexe,
        'elo' : player.elo,
        'id' : player.id,
        'score' : player.score,
        'opponents' : player.opponents
        }
        return serialized_player

    def _deserialized(self, serialized_players):
        players = []
        def _deserialized_step(serialized_player):
            first_name = serialized_player['first_name']
            last_name = serialized_player['last_name']
            date_birth = serialized_player['date_birth']
            sexe = serialized_player['sexe']
            elo = serialized_player['elo']
            id = serialized_player['id']
            score = serialized_player['score']
            opponents = serialized_player['opponents']
            player = Player(first_name=first_name, last_name=last_name,
                            date_birth=date_birth, sexe=sexe, elo=elo,
                            score=score)
            player.id = id
            player.opponents = opponents
            players.append(player)

        for serialized_player in serialized_players:
            _deserialized_step(serialized_player)
        return players

    def insert_player(self, player):
        self.players_table.insert(self._serialized(player))

    def load(self):
        serialized_players = self.players_table.all()
        return self._deserialized(serialized_players)

    def remove(self, player):
        if self.search(player):
            Person = Query()
            self.players_table.remove(Person.last_name == player)
            print (f'{player} à été supprimé')
            self.display()
        else:
            print (f"{player} n'existe pas dans la liste" )

    def update(self, player, arg, new_value):
        if self.search(player):
            Person = Query()
            self.players_table.update({arg: new_value}, Person.last_name == player)
            print (f'{player} a maintenant {new_value}')
            self.display()
        else:
            print (f"{player} n'existe pas dans la liste" )

    def display(self):
        for i in self.load():
            print (i.__dict__)

    def get(self, *args):
        for i in self.load():
            for arg in args:
                print (i.__dict__[arg])

    def read(self, player):
        print (player)

"""
round_1 = DataTournamentPlayers(run.get_infos_tournament().name_tournament,
                                        run.get_infos_tournament().rounds[0].round_name)
    matchs_in_round_1 = run.get_infos_tournament().rounds[0].matchs

    for player in matchs_in_round_1:
        round_1.insert_player(player.player1)
        round_1.insert_player(player.player2)
"""