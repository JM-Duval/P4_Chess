# -*-coding: utf-8 -*
#! /usr/bin/env python
"""This file is a exercice about a program for help the chess tournament organization.
It is a first program with MVC structuring."""

class Player:

    def __init__(self, first_name, last_name, date_birth, sexe, elo, score = 0):
        self.first_name = first_name
        self.last_name = last_name
        self.date_birth = date_birth
        self.sexe = sexe
        self.elo = elo
        self.score = score
        self.id = self.create_id()
        self.opponents = []


    def create_id(self):
        return str('@') + str(self.first_name)[:3].lower() + str(self.elo)

    def get_name(self):
        return self.first_name

    def get_score(self):
        return self.score

    def add_score(self, add_score):
        self.score += add_score

    def __str__(self):
        out_test = f"{self.first_name}-{self.last_name}"
        out = f"first name: {self.first_name} | last name: {self.last_name}, \n" \
              f"date of birth: {self.date_birth} | sexe: {self.sexe} \n " \
              f"score: {self.score} | elo: {self.elo} | id: {self.id} \n" \
              f"| opponents: {self.opponents}"
        return out_test

    def add_opponent(self, opponent_id):
        self.opponents.append(opponent_id)

    def clean_opponents(self):
        del self.opponents

    def __eq__(self, other):
        if self.id == other.id:
            return True
        else:
            return False