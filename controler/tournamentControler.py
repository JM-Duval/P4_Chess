# -*-coding: utf-8 -*
#! /usr/bin/env python
"""This file is a exercice about a program for help the chess tournament organization.
It is a first program with MVC structuring."""

from math import floor
import datetime
import sys
sys.path[:0]=['../']
from model.tournament import Tournament
from model.round import Round
from model.match import Match
from model.player import Player
from view.tournamentView import *
from view.rankingView import display_score, display_winner
from view.gamesheetView import *


player1 = Player('Annie', 'Cordy', '16/06/1928', 'w', 8)  #9
player2 = Player('Eric', 'Zemmour', '31/08/1958', 'm', 3) #4
player3 = Player('Jennifer', 'Lopez', '24/07/1969', 'w' , 4) #6
player4 = Player('Jacques', 'Chirac', '29/11/1932', 'm' , 5) #5
player5 = Player('Albert', 'Einstein', '14/03/1879', 'm', 1) #1
player6 = Player('Elycia', 'Marie',  '30/03/1986', 'w' , 2) #2
player7 = Player('Rachel', 'McAdams', '17/11/1978', 'w', 7) #8
player8 = Player('Arnold', 'Schwarzenegger', '30/07/1947', 'm' , 6) #7
player9 = Player('Donald', 'Trump', '14/06/1946', 'm' , 10) #10
player10 = Player('Brad', 'Pitt', '18/12/1963', 'm', 13) #3
players = [player1,player2,player3,player4,player5,player6,player7,player8]


class TournamentControler:

    def __init__(self):
        self.start_time = self.start_tournament()
        self.tournament_name, location, tour_number, time_control \
            = data_tournament()
        self.tournament = Tournament(self.tournament_name, location,
                                     self.start_time, tour_number, time_control)
        self.tournament.players = players
        self.nb_match = floor((len(self.tournament.players)/2))

    def start_tournament(self):
        start_time = datetime.datetime.today().strftime('%d-%m-%y at %H:%M')
        display_start_time(start_time)
        return start_time

    def close_tournament(self):
        end_time = datetime.datetime.today().strftime('%d-%m-%y at %H:%M')
        display_winner(self.tournament_name,
                       self.tournament.players[0].first_name)
        display_end_time(end_time)
        return end_time

    def run_first_round(self, round_name):
        #display_start_time(self.start_time)
        display_round(round_name)
        self.tournament.players.sort(key=lambda x: x.elo)
        round1 = Round(str(1))
        self.tournament.add_round(round1)
        for i in range (self.nb_match):
            round1.add_match(self.tournament.players[i],
                             self.tournament.players[i+self.nb_match])

        for match in round1.matchs: # add id player in opponent_list
            match.player1.add_opponent(match.player2.id)
            match.player2.add_opponent(match.player1.id)

        display_game_sheet('Round 1', round1.matchs)

        for i in range (self.nb_match): # for each match in round1, add score player
            self.handle_score(round1.matchs[i].player1,
                              round1.matchs[i].player2)
        #round1.matchs[0].score_player1, round1.matchs[0].score_player2 =
        # self.handle_score(player1, player2)

    def run_next_round(self, round_name):
        display_round(round_name)
        self.tournament.players.sort(key=lambda x: x.elo)
        self.tournament.players.sort(key=lambda x: x.score, reverse=True)
        roundx = Round(round_name)

        x = 0
        for i in range(floor(len(self.checked_opponents())/2)):
            roundx.add_match(self.checked_opponents()[i+x],
                             self.checked_opponents()[i+x+1])
            x += 1

        for match in roundx.matchs: # add id player in opponent_list
            match.player1.add_opponent(match.player2.id)
            match.player2.add_opponent(match.player1.id)

        display_score(self.tournament.players)
        display_game_sheet(round_name, roundx.matchs)

        for i in range (self.nb_match):
            self.handle_score(roundx.matchs[i].player1,
                              roundx.matchs[i].player2)
        display_score(self.tournament.players)

    def checked_opponents(self):
        players_sorted = []
        for i in self.tournament.players:
            players_sorted.append(i)
        opponent_list_checked = []
        while len(players_sorted) > 1:
            x = 0
            i = x
            opponent_in_list = True
            while opponent_in_list:
                try:
                    i += 1
                    if players_sorted[i].id in players_sorted[x].opponents:
                        opponent_in_list = True
                    else:
                        opponent_list_checked.append(players_sorted[x])
                        opponent_list_checked.append(players_sorted[i])
                        players_sorted.pop(x), players_sorted.pop(i - 1)
                        opponent_in_list = False
                except:  # situation ou un joueur à déja joué vs tout le monde.
                    # il rejoue vs le joueur n+1
                    opponent_list_checked.append(players_sorted[x])
                    opponent_list_checked.append(players_sorted[x+1])
                    players_sorted.pop(x), players_sorted.pop(x)
                    break
        return opponent_list_checked

    def handle_score(self, player1, player2):
        result_score = enter_score(player1, player2)
        player1.score += result_score[0]
        player2.score += result_score[1]


