# -*-coding: utf-8 -*
#! /usr/bin/env python
"""This file is a exercice about a program for help the chess tournament organization.
It is a first program with MVC structuring."""


class Round:

    def __init__(self, round): # round est une liste de match
        self.round = round

    def create_match(self):
        for i in range(4):
            self.round.append([])
        return self.round
























"""
    def __init__(self, match1, match2, match3, match4):
        #self.round_name = round_name
        self.match1 = match1
        self.match2 = match2
        self.match3 = match3
        self.match4 = match4

    def create_round(self):
        round = []
        round.append(self.match1)
        round.append(self.match2)
        round.append(self.match3)
        round.append(self.match4)
        return round

#a = Round("Rounds", 10)
#b = a.create_round('jo','fred')

round_name,
start_time = automatique,
end_time = automatique,
"""