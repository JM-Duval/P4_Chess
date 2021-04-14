# -*-coding: utf-8 -*
#! /usr/bin/env python
"""This file is a exercice about a program for help the chess tournament organization.
It is a first program with MVC structuring."""

from math import floor
import sys
sys.path[:0]=['../']
from model.tournament import Tournament
from model.round import Round
from model.match import Match
from model.player import Player
from view.tournamentView import enter_score


player1 = Player('Anna', 8, 8)  #9
player2 = Player('Eric', 22, 3) #4
player3 = Player('Sandra', 18, 4) #6
player4 = Player('Chirac', 18, 5) #5
player5 = Player('Albert', 25, 1) #1
player6 = Player('Marine', 24, 2) #2
player7 = Player('Rachel', 13, 7) #8
player8 = Player('Michel', 16, 6) #7
player9 = Player('Trump', 3, 10) #10
player10 = Player('Brad', 24, 13) #3
infos_players = [player1,player2,player3,player4,player5,player6,player7,player8]


class TournamentControler:

    def __init__(self):
        self.tournament = Tournament('La ronde des palets', 'Bullet')
        self.tournament.players = infos_players
        self.nb_match = floor((len(self.tournament.players)/2))

    def run_first_round(self):
        self.tournament.players.sort(key=lambda x: x.elo)
        round1 = Round(str(1))
        self.tournament.add_round(round1)
        for i in range (self.nb_match):
            round1.add_match(self.tournament.players[i],
                             self.tournament.players[i+self.nb_match])
        for i in range (self.nb_match): # for each match in round1, add score player
            self.handle_score(round1.matchs[i].player1,
                              round1.matchs[i].player2)
        #round1.matchs[0].score_player1, round1.matchs[0].score_player2 = self.handle_score(player1, player2)

    def handle_score(self, player1, player2):
        result_score = enter_score(player1, player2)
        if result_score == str(1):
            player1.score +=1
            print (f'{player1.first_name}: + 1 pt soit {player1.score}')
            #return 1,0
        elif result_score == str(2):
            player2.score += 1
            print(f'{player2.first_name}: +1 pt soit {player1.score}')
            #return 0,1
        elif result_score == str(3):
            player1.score += 0.5
            player2.score += 0.5
            print(f'Match Nul \n'
                  f'{player1.first_name}: +0.5 pts soit {player1.score}\n'
                  f'{player2.first_name}: +0.5 pts soit {player2.score}')
            #return 0.5,0.5





# -- run test ----------------------------
run = TournamentControler()
test = run.run_first_round()


"""
class LaunchNewTournament:

    def __init__(self, name_tournament, time, infos_players):
        self.name_tournament = name_tournament
        self.time = time
        self.infos_players = infos_players

    def create_players(self):
        players = []
        for infos_player in self.infos_players:
            player = model_player.Player(infos_player[0],
                                         infos_player[1],
                                         infos_player[2])
            players.append(player)
        return players

    def sorted_players_round1(self):
        sorted_players_round1 = self.create_players()
        sorted_players_round1.sort(key=lambda x: x.elo)
        return sorted_players_round1

    def sorted_players_rounds(self):
        sorted_players_rounds = self.create_players()
        sorted_players_rounds.sort(key=lambda x: x.score, reverse=True)
        sorted_players_rounds.sort(key=lambda x: x.elo)
        return sorted_players_rounds

    def nb_match(self):
        nb_match = floor(len(self.infos_players)/2)
        return nb_match

    def create_match(self, player1, player2):
        call_match = model_match.Match(player1, player2)
        match = call_match.create_match()
        return match

    def create_round1(self):
        call_round = model_round.Round(self.sorted_players_round1(), self.nb_match(), 'round1')
        round = call_round.create_round()
        return round

    def create_round(self, round):
        call_round = model_round.Round(self.sorted_players_rounds(), self.nb_match(), 'round1', round)
        round = call_round.create_round()
        return round

    def create_tournament(self):
        call_tournament = model_tournament.Tournament (self.sorted_players_round1(), 4)
        rounds = call_tournament.create_round()
        round1 = self.create_round(rounds[0])
        #print (round1)
        return round1

    def test_collect_winner_match(self, round1):
        collect_winner_match = dataUsers.DataUsers()
        winner_match = collect_winner_match.write_results_match(round1)
        print (winner_match)

    def run(self):
        #tour = self.create_tournament()
        player = self.test_collect_winner_match(self.create_tournament())
        print (player)


# -- run ------------------------
new_tournament = LaunchNewTournament ('tournoi 1', '9h00', infos_players)
new_tournament.run()
"""