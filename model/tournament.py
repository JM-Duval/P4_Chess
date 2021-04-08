# -*-coding: utf-8 -*
#! /usr/bin/env python
"""This file is a exercice about a program for help the chess tournament organization.
It is a first program with MVC structuring."""

class Tournament:

    def __init__(self):
        pass

    def create_tournament():
        list_rounds = []
        for i in range(4):
            name_round = 'Round' + str(i + 1)
            list_rounds.append(name_round)
        return list_rounds

#a = Tournament
#b = a.create_tournament()
#print (b)


"""
def __init__(self,
                 name,
                 location,
                 start_date,
                 end_date,
                 nbr_of_tours = 4,
                 rounds,
                 players,
                 time
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