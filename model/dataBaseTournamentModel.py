# -*-coding: utf-8 -*
#! /usr/bin/env python
"""This file is a exercice about tinydb.
Web_site_link = https://www.docstring.fr/blog/tinydb-une-base-de-donnees-adaptee-vos-projets/"""

from tinydb import TinyDB, Query, where
import sys
sys.path[:0]=['../']
import os
from model.player import Player
from model.tournament import Tournament
# TinyDB is the database
# Query allows to query the data base
# where allows to refine the search


class DataTournament:
    def __init__(self, tournament_name):
        self.tournament_name = tournament_name
        self.name_table = "data_tournament"
        self.name_file = self.tournament_name + '.json'
        origin_path = (sys.path[(len(sys.path)) -2][:-4])
        path_data_tournament = os.path.join(origin_path, 'data/tournaments')
        #path_data_tournament = Path("data/tournaments")
        db = TinyDB(os.path.join(path_data_tournament,self.name_file))
        self.tournament_table = db.table(self.name_table)

    def search(self, infos):
            Infos = Query()
            if self.tournament_table.search(Infos.tournament_name == self.tournament_name):
                return True
            else:
                return False

    def _serialized(self, infos_tour):
        serialized_infos_tour = {
        'tournament_name': infos_tour.tournament_name,
        'start_time': infos_tour.start_time,
        'tour_number': infos_tour.tour_number,
        'location': infos_tour.location,
        'time_control': infos_tour.time_control,
        'status': infos_tour.status
        }
        return serialized_infos_tour

    def _deserialized(self, serialized_infos_tour):
        infos_tournament = []
        def _deserialized_step(serialized_info_tour):
            tournament_name = serialized_info_tour['tournament_name']
            start_time = serialized_info_tour['start_time']
            tour_number = serialized_info_tour['tour_number']
            location = serialized_info_tour['location']
            time_control = serialized_info_tour['time_control']
            status = serialized_info_tour['status']
            tournament = Tournament(tournament_name=tournament_name,
                                    start_time=start_time,
                                    tour_number=tour_number,
                                    location=location,
                                    time_control=time_control,
                                    status=status)
            infos_tournament.append(tournament)
        for serialized_info_tour in serialized_infos_tour:
            _deserialized_step(serialized_info_tour)
        return infos_tournament

    def insert(self, infos_tour):
        self.tournament_table.insert(self._serialized(infos_tour))

    def load(self):
        serialized_infos_tour = self.tournament_table.all()
        return self._deserialized(serialized_infos_tour)

    def status(self):
        return self.load()[0].status

    def infos(self):
        return self.load()

class DataTournamentPlayers:
    def __init__(self, tournament_name, round_name):
        self.tournament_name = tournament_name
        self.name_table = round_name
        self.name_file = self.tournament_name+'.json'
        origin_path = (sys.path[(len(sys.path)) - 2][:-4])
        path_data_players = os.path.join(origin_path, 'data/tournaments')
        #path_data_players = Path("data/tournaments")
        db = TinyDB(os.path.join(path_data_players,self.name_file))
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

    def sorted_alpha(self):
        return sorted(self.load(), key=lambda x: x.last_name)

    def sorted_score(self):
        return sorted(self.load(), key=lambda x: x.score, reverse=True)






#--------------------------------------------------------------------------
"""
    def __init__(self, tournament_name): #, location, start_time, tour_number, time_control, status):
        self.tournament_name = tournament_name
        #self.location = location
        #self.start_time = start_time
        #self.tour_number = tour_number
        #self.time_control = time_control
        #self.status = status
        self.name_table = "data_tournament"
        self.name_file = self.tournament_name+'.json'
        path_data_tournament = Path("../data/tournaments")
        db = TinyDB(path_data_tournament / self.name_file)
        self.tournament_table = db.table(self.name_table)

    def record(self, location, start_time, tour_number, time_control, status):
        self.tournament_table.insert({'tournament_name': self.tournament_name,
                                      'start_time': start_time,
                                      'tour_number' : tour_number,
                                      'location': location,
                                      'time_control': time_control,
                                      'status' : status})

"""