# -*-coding: utf-8 -*
#! /usr/bin/env python
"""This file is a exercice about a program for help the chess tournament organization.
It is a first program with MVC structuring."""

class Tournament:

    def __init__(self, tournament_name, location, start_time, tour_number, time_control, status=None):
        self.tournament_name = tournament_name
        self.location = location
        self.start_time = start_time
        self.tour_number = tour_number
        self.time_control = time_control
        self.players = []
        self.rounds = []
        self.description = None
        self.status = status

    def __str__(self):
        out = f"{self.tournament_name}, {self.location}, {self.start_time}," \
              f"{self.tour_number},{self.time_control}, {self.rounds}, " \
              f"{self.players},{self.status}"
        return out

    def add_player(self, player):
        self.players.append(player)

    def add_round(self, round):
        self.rounds.append(round)
