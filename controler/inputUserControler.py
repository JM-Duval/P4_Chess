# -*-coding: utf-8 -*
#! /usr/bin/env python
"""This file is a exercice about a program for help the chess tournament organization.
It is a first program with MVC structuring."""


import datetime
import sys
#sys.setrecursionlimit(15000)
sys.path[:0]=['../']

from view.inputUserView import *
from model.inputUserModel import CheckerData


class UserInput:
    def __init__(self):
        pass

    def infos_tournament(self):
        tournament_name = 'Tournoi gp'#self.word('tournament_name') #'Word_tour_Tournament_13' #'Word_tour_Moto_GP'
        location = 'France_Le_Mans' #self.check_word('location')
        tour_number = 0
        time_control = '2'#self.time_control()
        rounds = []
        players = []
        note = ()
        return tournament_name, location, tour_number, time_control

    def infos_player(self):
        first_name = self.word('first name player')
        last_name = self.word('last name player')
        year_of_birth = self.year_of_birth()
        sexe = self.sexe()
        elo = self.number('elo')
        return first_name, last_name, year_of_birth, sexe, elo


    def word(self, word):
        user_input = enter(word)
        check_word = CheckerData(user_input).word()
        while check_word == False:
            display_error_word_message()
            user_input = enter(word)
            check_word = CheckerData(user_input).word()
        return user_input

    def number(self, number):
        user_input = enter(number)
        check_number = CheckerData(user_input).number()
        while check_number == False:
            display_error_number_message()
            user_input = enter(number)
            check_number = CheckerData(user_input).number()
        return int(user_input)

    def year_of_birth(self):
        year_birt_min = int(datetime.datetime.today().strftime('%Y')) - 120
        year_birt_max = int(datetime.datetime.today().strftime('%Y')) - 10
        user_input = enter('year of birth (DD-MM-YYYY)')
        check_year_of_birth = CheckerData(user_input).date()
        while check_year_of_birth == False:
            display_error_year_of_birth_message(year_birt_min, year_birt_max)
            user_input = enter('year of birth (DD-MM-YYYY)')
            check_year_of_birth = CheckerData(user_input).date()
        return user_input

    def sexe(self):
        user_input = enter("Man or Women :").lower()
        check_sexe = CheckerData(user_input).sexe()
        while check_sexe == False:
            display_error_sexe_message()
            user_input = enter("Man or Women :").lower()
            check_sexe = CheckerData(user_input).sexe()
        return user_input

    def time_control(self):
        display_time_control_selection()
        user_input = enter()
        check_time_control = CheckerData(user_input).time_control()
        while check_time_control == False:
            display_error_message()
            display_time_control_selection()
            user_input = input()
            check_time_control = CheckerData(user_input).time_control()
        return user_input

    def score(self, player1, player2):
        display_question_winner(player1, player2)
        user_input = enter()
        check_score = CheckerData(user_input).score()
        while check_score == False:
            display_error_message()
            display_question_winner(player1, player2)
            user_input = enter()
            check_score = CheckerData(user_input).score()

        if user_input == str(1):
            display_winner(player1)
            return 1, 0

        elif user_input == str(2):
            display_winner(player2)
            return 0, 1

        elif user_input == str(3):
            display_winners(player1, player2)
            return 0.5, 0.5

    def interval(self, number_max):
        while True:
            display_interval(number_max)
            user_input = enter()
            try:
                if  0 < int(user_input) <= number_max:
                    break
            except ValueError:
                if user_input.upper() == 'Q':
                    break
        return user_input
