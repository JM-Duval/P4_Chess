# -*-coding: utf-8 -*
#! /usr/bin/env python
"""This file is a exercice about a program for help the chess tournament organization.
It is a first program with MVC structuring."""

from math import floor

class Tournament:

    def __init__(self, name_tournament, time_control):
        self.name_tournament = name_tournament
        self.time_control = time_control
        self.players = []
        self.rounds = []

        #self.name_tournament = name_tournament
        #self.location = location
        #self.start_date = start_date
        #self.end_date = end_date
        #self.nb_rounds = nb_rounds
        #self.round = round   # rounds = liste des instances
        #self.players = players   # liste des players
        #self.time = time   # bullet
        #self.description = None

    def add_player (self, player):
        self.players.append(player)

    def add_round (self, round):
        self.rounds.append(round)








    def create_round(self):
        for i in range(self.nb_rounds):
            self.rounds.append([])
        return self.rounds