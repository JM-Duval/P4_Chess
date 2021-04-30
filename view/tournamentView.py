# -*-coding: utf-8 -*
#! /usr/bin/env python
"""This file is a exercice about a program for help the chess tournament organization.
It is a first program with MVC structuring."""

import datetime
import sys
sys.path[:0]=['../']
from controler.checkerInputControler import CheckerData

# ---------------------- Data tournament ---------------------------
def data_input_tournament():
    tournament_name = 'Word_tour_Tournament_2' #enter_word('tournament_name')
    location = 'Sydney' #enter_word('location')
    tour_number = 4
    time_control = '1' #input('Bullet / Blitz / Coup rapide :')
    rounds = []
    players = []
    note = ()
    return tournament_name, location, tour_number, time_control

def enter_time_control(controler):
    controler_input = input(f"{controler} : ")
    check = CheckData(controler_input)
    while check.time_control() == False:
        controler_input = input(f"{controler} : ")
        check = CheckData(controler_input)
    return controler_input

# ----------------------- Data player ------------------------------
def data_player():
    first_name = enter_word('first name player')
    last_name = enter_word('last name player')
    year_of_birth = enter_year_of_birth()
    sexe = enter_sexe()
    elo = enter_number('elo')
    return first_name, last_name, year_of_birth, sexe, elo

def enter_word(word):
    word_input = input(f"{word} : ")
    check = CheckData(word_input)
    while check.word() == False:
        print(
            " Saisir un mot ou groupe de mots suivant les conditions ci dessous : \n"
            " - Minimum 2 lettres \n"
            " - Caractères autorisés: abcdefghijklmnopqrstuvwxyz_ \n"
            " - Tout en minuscule"
            " - '_' remplace les espaces")
        word_input = input(f"{word} : ")
        check = CheckData(word_input)
    return word_input

def enter_number(number):
    nb = input(f"{number} : ")
    check = CheckData(nb)
    while check.number() == False:
        print(" Saisir un nombre suivant les conditions ci dessous : \n"
              " - Pas d'espace \n"
              " - Caractères autorisés: 1234567890")
        nb = input(f"{number} : ")
        check = CheckData(nb)
    return nb

def enter_year_of_birth():
    year_birt_min = int(datetime.datetime.today().strftime('%Y')) - 120
    year_birt_max = int(datetime.datetime.today().strftime('%Y')) - 10
    year_of_birth = input('year of birth (DD-MM-YYYY) :')
    check_year_of_birth = CheckData(year_of_birth)
    while check_year_of_birth.date() == False:
        print(
            f'Saisir une date de naissance suivant les conditions ci dessous : \n'
            f' - Année comprise entre : {year_birt_min} & {year_birt_max} \n'
            f' - Format : DD-MM-YYYY')

        year_of_birth = input('year of birth :')
        check_year_of_birth = CheckData(year_of_birth)
    return year_of_birth

def enter_sexe():
    sexe = input("Man or Women :").lower()
    check_sexe = CheckData(sexe)
    while check_sexe.sexe() == False:
        print("Saisir 'man' or 'women'")
        sexe = input("Man or Women :")
        check_sexe = CheckData(sexe)
    return sexe

# -------------------- Enter Score ---------------------
def enter_score(player1, player2):
    winner = str(2)
    """
    winner = input(f'\nQui a gagne? \n'
                   f'| {player1.first_name}  \t| : tapez 1 \n'
                   f'| {player2.first_name}  \t| : tapez 2 \n'
                   f'| match nul \t| : tapez 3 \n')

    while winner not in [str(1), str(2), str(3)]:
        print("Veuillez saisir un chiffre donné dans l'énoncé")
        winner = input(f'\nQui a gagne? \n'
                       f'| {player1.first_name}  \t| : tapez 1 \n'
                       f'| {player2.first_name}  \t| : tapez 2 \n'
                       f'| match nul \t| : tapez 3 \n')
    """
    if winner == str(1):
        print(f'{player1.first_name}: + 1 pt')
        return 1, 0

    elif winner == str(2):
        print(f'{player2.first_name}: + 1 pt')
        return 0, 1

    elif winner == str(3):
        print(f'{player1.first_name}\t: +0.5 pts\n'
              f'{player2.first_name}\t: +0.5 pts')
        return 0.5,0.5
