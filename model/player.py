# -*-coding: utf-8 -*
#! /usr/bin/env python
"""This file is a exercice about a program for help the chess tournament organization.
It is a first program with MVC structuring."""

class Player:

    def __init__(self,first_name, score, elo, last_name='nc'):
        self.first_name = first_name
        self.last_name = last_name
        self.score = score
        self.elo = elo

    def get_name(self):
        return self.first_name

    def set_score(self, add_score):
        self.score += add_score

    def get_score(self):
        return self.score

    def __str__(self):
        out = f"first name: {self.first_name} | last name: {self.last_name}," \
              f" | score: {self.score} | elo: {self.elo}"
        return out
