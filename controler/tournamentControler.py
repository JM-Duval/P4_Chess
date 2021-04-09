# -*-coding: utf-8 -*
#! /usr/bin/env python
"""This file is a exercice about a program for help the chess tournament organization.
It is a first program with MVC structuring."""

from math import floor
import sys
sys.path[:0]=['../']
from model import tournament as model_tournament
from model import round as model_round
from model import match as model_match
from model import player as model_player


class LaunchNewTournament:

    def __init__(self, name_tournament, time, infos_players):
        self.name_tournament = name_tournament
        self.time = time
        self.infos_players = infos_players

    def create_players(self):
        players = []
        for infos_player in self.infos_players:
            player = model_player.Player(infos_player[0], infos_player[1], infos_player[2])
            players.append(player)
            #print (player.first_name)
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
        #print (nb_match)

    def create_matchs(self):
        matchs = []
        for i in range (self.nb_match()):
            call_match = model_match.Match(self.sorted_players_rounds()[i], self.sorted_players_rounds()[i+self.nb_match()])
            match = call_match.create_match()
            matchs.append(match)
            #print (match)
        return matchs

    def create_round(self):
        call_round = model_round.Round(self.create_matchs()[0],self.create_matchs()[1],self.create_matchs()[2],self.create_matchs()[3])
        round = call_round.create_round()
        print ('Round 1 : ', round)







    def create_tournament(self):
        tournament = model_tournament.Tournament()
        rounds = tournament.create_tournament()
        print (rounds)
        return rounds


    #def create_round_1(self):
    #    r1 = model_round.Round(rounds[0], self.nb_match())
    #    round1 = r1.create_round()
    #    for i in range(self.nb_match()):
    #        match = model_match.Match(sorted_list_players()[i],
    #                                  sorted_list_players()[nb_match + i])
    #        infos_match = match.create_match()
    #        round1.append(infos_match)
    #        i += 1
    #    return round1












player1 = ['Anna', 8, 8]  #9
player2 = ['Eric', 22, 3] #4
player3 = ['Sandra', 18, 4] #6
player4 = ['Chirac', 18, 5] #5
player5 = ['Albert', 25, 1] #1
player6 = ['Marine', 24, 2] #2
player7 = ['Rachel', 13, 7] #8
player8 = ['Michel', 16, 6] #7
player9 = ['Trump', 3, 10] #10
player10 = ['Brad', 24, 13] #3
infos_players = [player1,player2,player3,player4,player5,player6,player7,player8]

# -- run ------------------------
new_tournament = LaunchNewTournament ('tournoi 1', '9h00', infos_players)
#new_tournament.create_players()
#new_tournament.sorted_players_round1()
#new_tournament.nb_match()
new_tournament.create_matchs()
new_tournament.create_rounds()

"""
# -- data ----------------------------------------
new_tournament = model_tournament.Tournament
rounds = new_tournament.create_tournament()
#print (tournoi)

#b = model_round.Round('Rounds 1 :')
#round = b.create_round()
#print ('Round : ', round)

#c = model_match.Match('Player 1', 'Player 2')
#match = c.create_match()
#print (match)


# -- sorted_list ---------------------------------
list_players = model_player.list_players()

def sorted_list_players():
    list_players.sort(key=lambda x: x.elo)
    list_players.sort(key=lambda x: x.score, reverse = True)
    players = []
    for player in list_players:
        players.append(player)
    return players

nb_match = floor(len(sorted_list_players())/2)


# -- Round_1 -------------------------------------
def create_round_1():
    r1 = model_round.Round(rounds[0], nb_match)
    round1 = r1.create_round()
    for i in range (nb_match):
        match = model_match.Match(sorted_list_players()[i], sorted_list_players()[nb_match + i])
        infos_match = match.create_match()
        round1.append(infos_match)
        i +=1
    return round1

y = 1
for i in create_round_1():
    print (f'Round-1 Match{y} : {i}')
    y+=1
"""