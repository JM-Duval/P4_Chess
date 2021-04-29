# -*-coding: utf-8 -*
#! /usr/bin/env python
"""This file is a exercice about a program for help the chess tournament organization.
It is a first program with MVC structuring."""


class Tournament:

    def __init__(self, name_tournament, location, start_time, tour_number, time_control):
        self.name_tournament = name_tournament
        self.location = location
        self.start_time = start_time
        self.tour_number = tour_number
        self.time_control = time_control
        self.players = []
        self.rounds = []
        self.description = None

    def __str__(self):
        out = f"Tournament: {self.name_tournament}, {self.location}, {self.rounds[0].matchs[0]}, {self.rounds[0]}"
        return out

    def add_player(self, player):
        self.players.append(player)

    def add_round(self, round):
        self.rounds.append(round)
