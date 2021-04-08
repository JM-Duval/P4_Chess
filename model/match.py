# -*-coding: utf-8 -*
#! /usr/bin/env python
"""This file is a exercice about a program for help the chess tournament organization.
It is a first program with MVC structuring."""

class Match:

    def __init__(self, player1, player2, score_player1=0, score_player2=0):
        self.player1 = player1
        self.player2 = player2
        self.score_player1 = score_player1
        self.score_player2 = score_player2

    def info_player(self, player, score):
        player_dict = {}
        player_dict[player.get_name()] = score
        return player_dict

    def create_match(self):
        match = []
        match.append(self.info_player(self.player1, self.score_player1))
        match.append(self.info_player(self.player2, self.score_player2))
        return match


#a = Match("paul","jack", 4, 5)
#b = a.create_match()
#print (b)
