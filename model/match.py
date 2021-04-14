# -*-coding: utf-8 -*
#! /usr/bin/env python
"""This file is a exercice about a program f    or help the chess tournament organization.
It is a first program with MVC structuring."""

class Match:

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.score_player1 = 0
        self.score_player2 = 0

    def __str__(self):
        out = f'{self.player1}, {self.player2}'
        return out


    def info_player(self, player, score):
        #player_dict = {}
        #player_dict[player.get_name()] = score
        #return player_dict
        player_list = []
        player_list.append(player.get_name())
        player_list.append(score)
        return player_list

    def create_match(self):
        match = []
        match.append(self.info_player(self.player1, self.score_player1))
        match.append(self.info_player(self.player2, self.score_player2))
        return match

    def sav_match(self, player1, player2, score_player1, score_player2):
        list_player1 = []
        list_player2 = []
        list_player1.append(player1)
        list_player1.append(score_player1)
        list_player2.append(player2)
        list_player2.append(score_player2)
        match_played = (list_player1,list_player2)
        return match_played

