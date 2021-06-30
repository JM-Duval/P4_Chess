# -*-coding: utf-8 -*
# ! /usr/bin/env python
"""This file is a exercice about a program for help the chess tournament organization.
It is a first program with MVC structuring."""

from model.match import Match
import time


class Round:

    def __init__(self, round_name):
        self.round_name = round_name
        self.matchs = []
        self.start_time = self.start_time
        self.end_time = self.end_time

    def start_time(self):
        time_now = time.strftime("%a %d %B %Hh%M, Paris")
        start_time = {self.round_name, time_now}
        return start_time

    def end_time(self):
        time_now = time.strftime("%a %d %B %Hh%M, Paris")
        end_time = {self.round_name, time_now}
        return end_time

    def __str__(self):
        out = f"{self.matchs}"
        return out

    def add_match(self, player1, player2):
        match = Match(player1, player2)
        self.matchs.append(match)
