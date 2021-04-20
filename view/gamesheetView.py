# -*-coding: utf-8 -*
#! /usr/bin/env python
"""This file is a exercice about a program for help the chess tournament organization.
It is a first program with MVC structuring."""


# -- Feuille de match --
def print_game_sheet (round_name, matchs):
    match_number=1
    for i in matchs:
        print (f'\n{round_name} Match {match_number}:   | {i.player1.first_name} | vs | {i.player2.first_name} |')
        match_number +=1


# -- Liste des joueurs avec lequel le joueur à déjà joué --
def print_opponents (player):
    for opponent in player.opponents:
        print (f'{player.first_name} a deja joue vs {opponent}')