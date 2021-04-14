# -*-coding: utf-8 -*
#! /usr/bin/env python
"""This file is a exercice about a program for help the chess tournament organization.
It is a first program with MVC structuring."""

def enter_score(player1, player2):
    winner = input(f'Qui a gagne? \n'
                   f'{player1.first_name} >> tapez 1 \n'
                   f'{player2.first_name} >> tapez 2 \n'
                   f'match nul >> tapez 3 :')
    while winner not in [str(1), str(2), str(3)]:
        print("Veuillez saisir un chiffre donné dans l'énoncé")
        winner = input(f'Qui a gagne? \n'
                       f'{player1.first_name} >> tapez 1 \n'
                       f'{player2.first_name} >> tapez 2 \n'
                       f'match nul >> tapez 3 :')

    return winner
