# -*-coding: utf-8 -*
#! /usr/bin/env python
"""This file is a exercice about a program for help the chess tournament organization.
It is a first program with MVC structuring."""

import datetime

def infos_tournament():
    tournament_name = 'La ronde des palets' #input('Nom du tournoi : ')
    location = 'Sydney' #input('Lieu : ')
    start_time = datetime.datetime.today().strftime('%d-%m-%y at %H:%M')
    tour_number = 4
    time_control = 'Bullet' #input('Bullet / Blitz / Coup rapide :')
    list_rounds = []
    list_players = []
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

def print_matchs_round (round_name, matchs):
    match_number=1
    for i in matchs:
        print (f'\n{round_name} Match {match_number}:   | {i.player1.first_name} | vs | {i.player2.first_name} |')
        match_number +=1

def print_score_player(round_name, matchs):
    print (f' -- Score player before {round_name} -- \n')
    for i in matchs:
        print (f'| {i.player1.first_name} : {i.player1.score} |\n'
               f'| {i.player2.first_name} : {i.player2.score} |')
