# -*-coding: utf-8 -*
#! /usr/bin/env python
"""This file is a exercice about a program for help the chess tournament organization.
It is a first program with MVC structuring."""


# -- Date début & fin du tournoi --
def display_start_time(start_time):
    print (f'Lancement du tournoi: {start_time}')

def display_end_time(end_time):
    print (f'Fin du tournoi: {end_time}')

# -- Feuille de match --
def display_game_sheet (round_name, matchs):
    match_number=1
    for i in matchs:
        print (f'\n Match {match_number}:| {i.player1.first_name} \t|vs | {i.player2.first_name}\t|')
        match_number +=1


# -- Liste des joueurs avec lequel le joueur à déjà joué --
def display_opponents (player):
    for opponent in player.opponents:
        print (f'{player.first_name} a deja joue vs {opponent}')

# -- Affiche n° Round --
def display_round(round_name):
    print (f'\n*********  {round_name}  *********\n')

