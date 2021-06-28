# -*-coding: utf-8 -*
# ! /usr/bin/env python
"""This file is a exercice about a program for help the chess tournament organization.
It is a first program with MVC structuring."""

import datetime


class CheckerData:

    def __init__(self, data_input):
        self.data_input = data_input
        self.letters = "abcdefghijklmnopqrstuvwxyz_"
        self.numbers = "1234567890"
        self.year_birt_min = int(datetime.datetime.today().strftime('%Y')) - 120
        self.year_birt_max = int(datetime.datetime.today().strftime('%Y')) - 10
        self.list_sexe = {'man', 'women'}
        self.time_controler = {'1', '2', '3'}  # bullet // blitz // coup rapide

    def word(self):
        if len(self.data_input) < 2:
            return False

        for i in self.data_input:
            if i in self.letters:
                continue
            else:
                return False

    def number(self):
        for i in self.data_input:
            if i in self.numbers:
                continue
            else:
                return False

    def date(self):
        format = "%d-%M-%Y"
        year_date = self.data_input[-4:]
        try:
            datetime.datetime.strptime(self.data_input, format)
        except ValueError:
            return False
        if int(year_date) in range(self.year_birt_min, self.year_birt_max):
            return True
        else:
            return False

    def sexe(self):
        if self.data_input in self.list_sexe:
            return True
        else:
            return False

    def time_control(self):
        if self.data_input in self.time_controler:
            return True
        else:
            return False

    def score(self):
        if self.data_input in [str(1), str(2), str(3)]:
            return True
        else:
            return False
