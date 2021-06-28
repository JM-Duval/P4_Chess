# -*-coding: utf-8 -*
# ! /usr/bin/env python
"""This file is a exercice about a program for help the chess tournament organization.
It is a first program with MVC structuring."""


def enter(description='>'):
    user_input = input(f"{description} : ")
    return user_input


def display_error_word_message():
    print(
        " Saisir un mot ou groupe de mots suivant les conditions ci dessous : \n"
        " - Minimum 2 lettres \n"
        " - Caractères autorisés: abcdefghijklmnopqrstuvwxyz_ \n"
        " - Tout en minuscule"
        " - '_' remplace les espaces")


def display_error_number_message():
    print(" Saisir un nombre suivant les conditions ci dessous : \n"
          " - Pas d'espace \n"
          " - Caractères autorisés: 1234567890")


def display_error_year_of_birth_message(year_birt_min, year_birt_max):
    print(
        f'Saisir une date de naissance suivant les conditions ci dessous : \n'
        f' - Année comprise entre : {year_birt_min} & {year_birt_max} \n'
        f' - Format : DD-MM-YYYY')


def display_error_sexe_message():
    print("Saisir 'man' or 'women'")


def display_time_control_selection():
    print('Selectionnez un controleur de temps:\n'
          ' 1 - Bullet\n'
          ' 2 - Blitz\n'
          ' 3 - Coup rapide')


def display_question_winner(player1, player2):
    print('Vainqueur du match ?')
    print(f'| {player1.first_name}  \t| : tapez 1 \n'
          f'| {player2.first_name}  \t| : tapez 2 \n'
          f'| match nul \t| : tapez 3 \n')


def display_error_message():
    print("Oops! Saisie incorrect. Essayez à nouveau...")


def display_winner(player):
    print(f'{player.first_name}: + 1 pt')


def display_winners(player1, player2):
    print(f'{player1.first_name}: + 0.5 pt')
    print(f'{player2.first_name}: + 0.5 pt')


def display_interval(number_max):
    print()
    print(f'Selectionnez un nombre compris entre 1 & {number_max}')
    print('ou Q pour revenir au menu precedent.')


def display_back():
    print('ou Q pour revenir au menu precedent.')
