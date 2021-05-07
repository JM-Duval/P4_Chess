# -*-coding: utf-8 -*
#! /usr/bin/env python
"""This file is a exercice about tinydb.
Web_site_link = https://www.docstring.fr/blog/tinydb-une-base-de-donnees-adaptee-vos-projets/"""

from tinydb import TinyDB, Query, where
import sys
sys.path[:0]=['../']
import os
from model.player import Player
from model.match import Match
from model.round import Round
from model.tournament import Tournament

# TinyDB is the database
# Query allows to query the data base
# where allows to refine the search


class DataTournament:
    def __init__(self, tournament_name):
        self.tournament_name = tournament_name
        self.name_table = self.tournament_name
        self.name_file = 'tournaments.json'
        origin_path = (sys.path[(len(sys.path)) -2][:-4])
        path_data_tournament = os.path.join(origin_path, 'data/tournaments')
        #path_data_tournament = Path("data/tournaments")
        db = TinyDB(os.path.join(path_data_tournament,self.name_file))
        self.tournament_table = db.table(self.name_table)


    def _serialized_infos_tour(self, infos_tour):
        serialized_infos_tour = {
        'tournament_name': infos_tour.tournament_name,
        'start_time': infos_tour.start_time,
        'tour_number': infos_tour.tour_number,
        'location': infos_tour.location,
        'time_control': infos_tour.time_control,
        'status': infos_tour.status,
        'end_time' : infos_tour.end_time,
        'players' : (self._serialized_player(infos_tour.players[0]),
                     self._serialized_player(infos_tour.players[1]),
                     self._serialized_player(infos_tour.players[2]),
                     self._serialized_player(infos_tour.players[3]),
                     self._serialized_player(infos_tour.players[4]),
                     self._serialized_player(infos_tour.players[5]),
                     self._serialized_player(infos_tour.players[6]),
                     self._serialized_player(infos_tour.players[7])
                         )
        }
        return serialized_infos_tour

    def update(self, arg, new_value):
        Tour = Query()
        self.tournament_table.update({arg: new_value}, Tour.tournament_name == self.tournament_name)

    def _serialized_player(self, player):
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


    def serialized_round(self, round):
        serialized_round = {
                'Round' : (self.serialized_match(round.matchs[0]),
                           self.serialized_match(round.matchs[1]),
                           self.serialized_match(round.matchs[2]),
                           self.serialized_match(round.matchs[3])
                           )
                           }
        return serialized_round

    def serialized_match(self, match):
        serialized_match = {
            'match' : (self._serialized_player(match.player1),self._serialized_player(match.player2))
        }
        return serialized_match


    def _deserialized_infos_tour(self, serialized_infos_tour):
        infos_tournament = []
        def _deserialized_step(serialized_info_tour):
            tournament_name = serialized_info_tour['tournament_name']
            start_time = serialized_info_tour['start_time']
            tour_number = serialized_info_tour['tour_number']
            location = serialized_info_tour['location']
            time_control = serialized_info_tour['time_control']
            status = serialized_info_tour['status']
            end_time = serialized_infos_tour['end_time']
            players = self._deserialized_players(serialized_infos_tour['players'])

            tournament = Tournament(tournament_name=tournament_name,
                                    start_time=start_time,
                                    tour_number=tour_number,
                                    location=location,
                                    time_control=time_control,
                                    status=status,
                                    end_time=end_time
                                    )
            infos_tournament.append(tournament)
        for serialized_info_tour in serialized_infos_tour:
            _deserialized_step(serialized_info_tour)
        return infos_tournament

    def _deserialized_players(self, serialized_players):
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




    def insert_infos_tour(self, infos_tour):
        self.tournament_table.insert(self._serialized_infos_tour(infos_tour))

    def insert_round(self, round):
        self.tournament_table.insert(self.serialized_round(round))




"""

# -----------------------------------------
#self, tournament_name, location, start_time, tour_number, time_control, status=None
tour = Tournament('word championship', 'sydney', 'today', 4, 3, 'open')
test_save = DataTournament('word championship')
test_save.insert_infos_tour(tour)

#first_name, last_name, date_birth, sexe, elo
player_Rins = Player('Alex', 'Rins', '25', 'Man', 9)
player_Martin = Player('Jorge', 'Martin', '23', 'Man', 13)
player_Mir = Player('Joan', 'Mir', '23', 'Man', 4)
player_Rossi = Player('Valentino', 'Rossi', '42', 'Man', 21)
player_Miller = Player('Jack', 'Mille', '26', 'Man', 6)
player_Marquez = Player('Marc', 'Marquez', '28', 'Man', 15)
player_Zarco = Player('Johan', 'Zarco', '30', 'Man', 5)
player_Morbidelli = Player('Franco', 'Morbidelli', '26', 'Man', 8)
players = [player_Rins, player_Martin, player_Mir, player_Rossi, player_Miller, player_Marquez, player_Zarco, player_Morbidelli]
# ------------------------------------------
#test_save.insert_player(player_Rins)
#test_save.insert_player(player_Martin)
#test_save.insert_player(player_Mir)
#test_save.insert_player(player_Rossi)
test_save.insert_players(players)


match1 = Match(player_Mir,player_Rins)
match2 = Match(player_Martin,player_Rossi)
match3 = Match(player_Miller, player_Marquez)
match4 = Match(player_Zarco, player_Morbidelli)

round1 = Round ('Round1')
round1.add_match(player_Martin,player_Rossi)
round1.add_match(player_Rins,player_Mir)
round1.add_match(player_Miller, player_Marquez)
round1.add_match(player_Zarco, player_Morbidelli)

round1_test = tour.add_round(round1)
test_save.insert_round(round1)

"""









"""
    def load(self):
        serialized_infos_tour = self.tournament_table.all()
        return self._deserialized(serialized_infos_tour)

    def status(self):
        return self.load()[0].status

    def update(self, player, arg, new_value):
        if self.search(player):
            Person = Query()
            self.players_table.update({arg: new_value}, Person.last_name == player)
            print(f'{player} a maintenant {new_value}')
            self.display()
        else:
            print(f"{player} n'existe pas dans la liste")



    #def insert_match(self, match):
    #    self.tournament_table.insert(self.serialized_match(match))

    #def insert_player(self, player):
    #    self.tournament_table.insert(self._serialized_player(player))





"""




























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

    def search(self, infos):
            Infos = Query()
            if self.tournament_table.search(Infos.tournament_name == self.tournament_name):
                return True
            else:
                return False


"""