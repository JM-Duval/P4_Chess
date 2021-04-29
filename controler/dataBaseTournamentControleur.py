# -*-coding: utf-8 -*
#! /usr/bin/env python
"""This file is a exercice about tinydb.
Web_site_link = https://www.docstring.fr/blog/tinydb-une-base-de-donnees-adaptee-vos-projets/"""

from tinydb import TinyDB, Query, where
import sys
sys.path[:0]=['../']
from controler.tournamentControler import TournamentControler
from model.player import *
# TinyDB is the database
# Query allows to query the data base
# where allows to refine the search

class DataTournament:
    def __init__(self, tournament_name, name_table):
        self.tournament_name = tournament_name
        self.name_table = name_table
        self.name_file = self.tournament_name+'.json'
        db = TinyDB(self.name_file)
        self.tournament_table = db.table(self.name_table)

    def insert(self, data_tournament):
        self.tournament_table.insert(data_tournament)

    def search(self, player):
        pass


class DataTournamentPlayers:
    def __init__(self, tournament_name, name_table):
        self.tournament_name = tournament_name
        self.name_table = name_table
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


if __name__ == "__main__":

    test = DataTournamentPlayers('Word_tour_Tournament', 'Round 4')
    print(test.load()[0].first_name, test.load()[1].first_name)
    print(test.load()[2].first_name, test.load()[3].first_name)
    print(test.load()[4].first_name, test.load()[5].first_name)
    print(test.load()[6].first_name, test.load()[7].first_name)



    def winner (round, match):
        matchs = DataTournamentPlayers('Word_tour_Tournament', round)
        if match == 1:
            print(matchs.load()[0].first_name, matchs.load()[0].score,
                  matchs.load()[1].first_name, matchs.load()[1].score)
        elif match == 2:
            print(matchs.load()[2].first_name, matchs.load()[2].score,
                  matchs.load()[3].first_name, matchs.load()[3].score)
        elif match == 3:
            print(matchs.load()[4].first_name, matchs.load()[4].score,
                  matchs.load()[5].first_name, matchs.load()[5].score)
        elif match == 4:
            print(matchs.load()[6].first_name, matchs.load()[6].score,
                  matchs.load()[7].first_name, matchs.load()[7].score)


    winner('Round 2', 1)
    winner('Round 2', 2)
    winner('Round 2', 3)
    winner('Round 2', 4)

"""
    run = TournamentControler()
    run.start_tournament()

    # -- Data Round ------------------------
    data_tournament = DataTournament(run.get_infos_tournament().name_tournament, "data_tournament")
    data_tournament.insert({'tournament_name': run.get_infos_tournament().name_tournament,
                            'start_time': run.get_infos_tournament().start_time,
                            'location': run.get_infos_tournament().location,
                            'time_control': run.get_infos_tournament().time_control})

    # -- Round 1 ---------------------------
    run.run_first_round('Round 1')
    round_1 = DataTournamentPlayers(run.get_infos_tournament().name_tournament,
                                        run.get_infos_tournament().rounds[0].round_name)
    matchs_in_round_1 = run.get_infos_tournament().rounds[0].matchs
    print (matchs_in_round_1[0])


    for player in matchs_in_round_1:
        round_1.insert_player(player.player1)
        round_1.insert_player(player.player2)
    print (run.get_infos_tournament().rounds[0].round_name)



    # -- Other Rounds ----------------------
    for i in range(3):
        round_name = 'Round ' + str(i+2)
        run.run_next_round(round_name)
        roundx = DataTournamentPlayers(run.get_infos_tournament().name_tournament,
                                       run.get_infos_tournament().rounds[i+1].round_name)
        matchs_in_roundx = run.get_infos_tournament().rounds[i+1].matchs
        for player in matchs_in_roundx:
            roundx.insert_player(player.player1)
            roundx.insert_player(player.player2)
        print(run.get_infos_tournament().rounds[i+1].round_name)

    run.close_tournament()

"""







"""
    # -- Round 2 ---------------------------
    run.run_next_round('Round 2')
    round_2 = DataBaseTournament(run.get_infos_tournament().name_tournament, run.get_infos_tournament().rounds[1].round_name)
    matchs_in_round_2 = run.get_infos_tournament().rounds[1].matchs
    for player in matchs_in_round_2:
        round_2.insert_player(player.player1)
        round_2.insert_player(player.player2)
    print(run.get_infos_tournament().rounds[1].round_name)

    # -- Round 3 ---------------------------
    run.run_next_round('Round 3')
    round_3 = DataBaseTournament(run.get_infos_tournament().name_tournament, run.get_infos_tournament().rounds[2].round_name)
    matchs_in_round_3 = run.get_infos_tournament().rounds[2].matchs
    for player in matchs_in_round_3:
        round_3.insert_player(player.player1)
        round_3.insert_player(player.player2)
    print(run.get_infos_tournament().rounds[2].round_name)

    # -- Round 4 ---------------------------
    run.run_next_round('Round 4')
    round_4 = DataBaseTournament(run.get_infos_tournament().name_tournament,
                                 run.get_infos_tournament().rounds[
                                     3].round_name)
    matchs_in_round_4 = run.get_infos_tournament().rounds[3].matchs
    for player in matchs_in_round_4:
        round_4.insert_player(player.player1)
        round_4.insert_player(player.player2)
    print(run.get_infos_tournament().rounds[3].round_name)


    # -- Other Rounds ----------------------
    rounds = ['Round_2', 'Rounds_3', 'Rounds_4']
    x=1
    for round_name in rounds :
        #round_name = 'Round ' + str(2 + i)
        run.run_next_round(round_name)
        test = DataBaseTournament(run.get_infos_tournament().name_tournament,
                                  round_name)
        print (run.get_infos_tournament())
      
        matchs = run.get_infos_tournament().rounds[x].matchs
        for player in matchs:
            test.insert(player.player1)
            test.insert(player.player2)
        x +=1

    for i in range (4):
        round_name = 'Round '+str(i+1)
        test = DataTournamentPlayers('Word_tour_Tournament', round_name)
        x=0
        for i in test.load():
            print (i.first_name)

"""