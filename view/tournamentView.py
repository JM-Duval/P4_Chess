# -*-coding: utf-8 -*
#! /usr/bin/env python
"""This file is a exercice about a program for help the chess tournament organization.
It is a first program with MVC structuring."""

import datetime
import sys
sys.path[:0]=['../']


def display_start_time(start_time):
    print (f'Lancement du tournoi: {start_time}')

def display_end_time(end_time):
    print (f'Fin du tournoi: {end_time}')

def display_game_sheet(matchs):
    match_number=1
    for i in matchs:
        print (f'\n Match {match_number}:| {i.player1.first_name} \t|vs | {i.player2.first_name}\t|')
        match_number +=1

def display_opponents (player):
    for opponent in player.opponents:
        print (f'{player.first_name} a deja joue vs {opponent}')

def display_round(round_name):
    print (f'\n*********  {round_name}  *********')


def display_score(players):
    players.sort(key=lambda x: x.elo)
    players.sort(key=lambda x: x.score, reverse=True)
    print (f'\n------  Score Player  ------')
    for player in players:
        print (f'| {player.first_name}  \t{player.id}\t{player.score}  |')

def display_winner(tournament_name, player):
    print(' // Tournoi termine // ')
    print (f' Le vainqueur du tournoi "{tournament_name}" est : \n'
           f'****************  {player}  ****************')

def display_continue_tournament():
    print(' |> Souhaitez vous continuer?')
    print(' 1 - Oui')
    print(' Q - Retour')




"""
# -------------------- Enter Score ---------------------
def enter_score(player1, player2):
    winner = str(1)
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
    if winner == str(1):
        #print(f'{player1.first_name}: + 1 pt')
        return 1, 0

    elif winner == str(2):
        #print(f'{player2.first_name}: + 1 pt')
        return 0, 1

    elif winner == str(3):
        #print(f'{player1.first_name}\t: +0.5 pts\n'
        #      f'{player2.first_name}\t: +0.5 pts')
        return 0.5,0.5
"""