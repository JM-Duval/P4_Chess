# -*-coding: utf-8 -*
#! /usr/bin/env python
"""This file is a exercice about a program for help the chess tournament organization.
It is a first program with MVC structuring."""


class Round:

    def __init__(self, round_name, nb_match=4):
        self.round_name = round_name
        self.nb_match = nb_match

    def create_round(self):
        match = []
        #for i in range (self.nb_match):
        #    match.append([])
        #print (f'{self.round_name}', match)
        return match


#a = Round("Rounds", 10)
#b = a.create_round('jo','fred')
