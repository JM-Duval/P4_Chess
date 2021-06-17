# -*-coding: utf-8 -*
#! /usr/bin/env python
"""This file is a exercice about a program for help the chess tournament organization.
It is a first program with MVC structuring."""


# -- Classement --
def display_score(players):
    players.sort(key=lambda x: x.elo)
    players.sort(key=lambda x: x.score, reverse=True)
    print (f'\n------  Score Player  ------')
    for player in players:
        print (f'| {player.first_name}  \t{player.id}\t{player.score}  |')


# -- Vainqueur --
def display_winner(tournament_name, player):
    print(' // Tournoi terminé // ')
    print (f' Le vainqueur du tournoi "{tournament_name}" est : \n'
           f'****************  {player}  ****************')