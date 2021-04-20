# -*-coding: utf-8 -*
#! /usr/bin/env python
"""This file is a exercice about a program for help the chess tournament organization.
It is a first program with MVC structuring."""

import datetime

def data_tournament():
    tournament_name = 'La ronde des palets'
    location = 'Sydney'
    start_time = datetime.datetime.today().strftime('%d-%m-%y at %H:%M')
    tour_number = 4
    time_control = 'Bullet' #input('Bullet / Blitz / Coup rapide :')
    rounds = []
    players = []
    note = ()
    return tournament_name, location, start_time, tour_number, time_control


def enter_score(player1, player2):
    winner = input(f'\nQui a gagne? \n'
                   f'| {player1.first_name} | : tapez 1 \n'
                   f'| {player2.first_name} | : tapez 2 \n'
                   f'match nul : tapez 3 \n')
    while winner not in [str(1), str(2), str(3)]:
        print("Veuillez saisir un chiffre donné dans l'énoncé")
        winner = input(f'\nQui a gagne? \n'
                       f'| {player1.first_name} | : tapez 1 \n'
                       f'| {player2.first_name} | : tapez 2 \n'
                       f'match nul : tapez 3 \n')
    return winner


