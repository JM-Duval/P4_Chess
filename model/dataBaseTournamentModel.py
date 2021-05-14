# -*-coding: utf-8 -*
#! /usr/bin/env python
"""This file is a exercice about tinydb.
Web_site_link = https://www.docstring.fr/blog/tinydb-une-base-de-donnees-adaptee-vos-projets/"""

from tinydb import TinyDB, Query, where
import sys
sys.path[:0]=['../']
import os
from model.tournament import Tournament
from model.round import Round
from model.match import Match
from model.player import Player

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
        db = TinyDB(os.path.join(path_data_tournament,self.name_file))
        self.tournament_table = db.table(self.name_table)


    def serialized_tournament(self, tournament):
        serialized_tournament = {
        'tournament_name': tournament.tournament_name,
        'start_time': tournament.start_time,
        'tour_number': tournament.tour_number,
        'location': tournament.location,
        'time_control': tournament.time_control,
        'status': tournament.status,
        'end_time' : tournament.end_time,
        'players' : [self._serialized_player(player) for player in tournament.players],
        'rounds' : [self._serialized_round(round) for round in tournament.rounds]
        }
        return serialized_tournament

    def _serialized_round(self, round):
        return [self._serialized_match(match) for match in round.matchs]

    def _serialized_match(self, match):
        serialized_match = {
            'match' : (self._serialized_player(match.player1),
                      self._serialized_player(match.player2))
        }
        return serialized_match

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



# --------------------------------------------------------------


    def _deserialized_tournament(self, serialized_tournament):
        tournament_name = serialized_tournament['tournament_name']
        start_time = serialized_tournament['start_time']
        tour_number = serialized_tournament['tour_number']
        location = serialized_tournament['location']
        time_control = serialized_tournament['time_control']
        status = serialized_tournament['status']
        end_time = serialized_tournament['end_time']
        players = [self._deserialized_player(player) for player in serialized_tournament['players']]
        rounds = [self._deserialized_round(round) for round in serialized_tournament['rounds']]
        tournament = Tournament(tournament_name=tournament_name,
                                start_time=start_time,
                                tour_number=tour_number,
                                location=location,
                                time_control=time_control,
                                status=status,
                                end_time=end_time
                                )
        tournament.players = players
        tournament.rounds = rounds
        return tournament


    def _deserialized_round(self,serialized_round):
        round = Round('round')
        for i in range(len(serialized_round)):
            player1 = serialized_round[i]['match'][0]
            player2 = serialized_round[i]['match'][1]
            round.add_match(self._deserialized_player(player1),
                            self._deserialized_player(player2))
        return round

    def _deserialized_player(self, serialized_player):
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
        return player




    def load_tournament(self):
        serialized_tournament = self.tournament_table.all()[0]
        tournament = self._deserialized_tournament(serialized_tournament)
        return tournament

    def save_tournament(self, tournament):
        self.tournament_table.insert(self.serialized_tournament(tournament))

    def delete(self):
        self.tournament_table.truncate()













"""






    def deserialized_match(self, serialized_match):
        player1 = serialized_match['match'][0]
        player2 = serialized_match['match'][1]
        matchs = []
        match = Match(self._deserialized_player(player1),self._deserialized_player(player2))
        matchs.append(match)
        return match
        
        
    def _deserialized_rounds(self,serialized_rounds):
        rounds = []
        for i in range(len(serialized_rounds)-1):
            rounds.append(self._deserialized_round(serialized_rounds[i+1]))
        return rounds


    def _deserialized_players(self, serialized_players):
        players = []
        for serialized_player in serialized_players:
            players.append(self._deserialized_player(serialized_player))
        return players


    def update(self, arg, new_value):
        Tour = Query()
        self.tournament_table.update({arg: new_value}, Tour.tournament_name == self.tournament_name)
        print()

    def update_data_players(self): #, arg, new_value):
        #self.tournament_players = self.tournament_table.all()[0]['players'][0]
        #print(self.tournament_table.all()[0]['players'][0])
        Player = Query()
        #print(self.tournament_table.search(Player.players.last_name == 'Sydney')) #self.tournament_name))
        #print(self.tournament_table.update({'score' : 333}, Player.players == self.tournament_table.all()[0]['players'][0]))
        #print(self.tournament_table)
        pass





# --------------------------------------------------------------




    def add_round(self, round):
        print(round.matchs[0])
        self.tournament_table.insert(self._serialized_round(round))



    def insert_round(self, round):
        self.tournament_table.insert(self._serialized_round(round))
        #print(a)

    def load_rounds(self):
        serialized_rounds = self.tournament_table.all()
        return self._deserialized_rounds(serialized_rounds)












    def load_matchs(self):
        serialized_round = self.tournament_table.all()[1]
        serialized_matchx = serialized_round['Round']
        serialized_matchs = [serialized_matchx[0], serialized_matchx[1],
                             serialized_matchx[2], serialized_matchx[3]
                             ]
        return self.deserialized_matchs(serialized_matchs)



    def load_players(self):
        serialized_round = self.tournament_table.all()[1]
        serialized_matchs = serialized_round['Round']
        serialized_match = serialized_matchs[3]
        serialized_players = serialized_match['match']
        return self._deserialized_players(serialized_players)




        for key, value in serialized_infos_tour:
            if value["status"] == "open":
                print(f"id:{key}  |", value["tournament_name"], value["start_time"])




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




        def _deserialized_step(serialized_info_tour):
            pass
            #print (serialized_info_tour['players'][0])

            #for key, value in serialized_info_tour['players'][0].items():
            #    print(key,value)
                #print(value)
                #if value["status"] == "open":
                #print(f"id:{key}  |", value["first_name"], value["start_time"])

            
            tournament_name = serialized_info_tour['tournament_name']
            start_time = serialized_info_tour['start_time']
            tour_number = serialized_info_tour['tour_number']
            location = serialized_info_tour['location']
            time_control = serialized_info_tour['time_control']
            status = serialized_info_tour['status']
            end_time = serialized_info_tour['end_time']
            players = self._deserialized_players(serialized_info_tour['players'])

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

        #return infos_tournament
"""












"""
    def _serialized_roundx(self, round):
        rounds = []
        #self._serialized_round(round)
        rounds.append(self._serialized_round(round))
        return rounds



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
        #'rounds' : (self._serialized_round())
        }
        return serialized_infos_tour






    def _serialized_rounds(self, rounds):
        rounds_list = []
        for round in rounds:
            rounds_list.append(self._serialized_round(round))
        return rounds_list

        serialized_rounds = {
                'Rounds' : (self._serialized_round(rounds[0]),
                            self._serialized_round(rounds[1]),
                            self._serialized_round(rounds[2]),
                            self._serialized_round(rounds[3]),
                            )
        }
        return serialized_rounds



















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








        for serialized_match in serialized_matchs:
            serialized_players = serialized_match['match']
            match = self._deserialized_players(serialized_players)
            matchs.append(match)
        return matchs

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

    """