# -*-coding: utf-8 -*
#! /usr/bin/env python
"""This file is a exercice about a program for help the chess tournament organization.
It is a first program with MVC structuring."""

class Tournament:

    def __init__(self, round1, round2, round3, round4):
        self.round1 = round1
        self.round2 = round2
        self.round3 = round3
        self.round4 = round4

    def create_tournament(self):
        tournament = []
        tournament.append(self.round1)
        tournament.append(self.round2)
        tournament.append(self.round3)
        tournament.append(self.round4)
        return tournament

    def round_name(self):
        round_name = []
        for i in range(4):
            name_round = 'Round' + str(i + 1)
            round_name.append(name_round)
        return round_name



"""
a = Tournament()
b = a.create_tournament()
print (b)

def __init__(self,
                 name_tournament,
                 location,
                 start_date,
                 end_date,
                 nbr_of_rounds = 4,
                 rounds,
                 players,
                 time,
                 description
                 ):
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.nbr_of_tours = nbr_of_tours
        self.rounds = rounds
        self.players = players
        self.time = time
        self.description = None
"""