# -*-coding: utf-8 -*
#! /usr/bin/env python
"""This file is a exercice about a program for help the chess tournament organization.
It is a first program with MVC structuring."""

import sys
sys.path[:0]=['../']
from model.match import Match


class Round:

    def __init__(self, round_name):
         #self.list_players = list_players
         #self.nb_match = nb_match
         self.round_name = round_name
         self.matchs = []

        #self.round = round // liste de matchs
        #self.round_name = round_name
        #self.start_time = start_time
        #self.end_time = end_time

    def add_match(self, player1, player2):
        match = Match(player1,player2)
        self.matchs.append(match)

    def __str__(self):
        out = f"Match: {self.matchs[0]}"
        return out


    def create_round(self):
        for i in range (self.nb_match):
            call_match = model_match.Match(self.list_players[i],
                                           self.list_players[i + self.nb_match])
            match = call_match.create_match()
            self.round.append(match)
        return self.round

