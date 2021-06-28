# -*-coding: utf-8 -*
# ! /usr/bin/env python
"""This file is a exercice about a program for help the chess tournament organization.
It is a first program with MVC structuring."""

import sys
sys.path[:0] = ['../']


def display_start_time(start_time):
    print(f'Lancement du tournoi: {start_time}')


def display_end_time(end_time):
    print(f'Fin du tournoi: {end_time}')


def display_game_sheet(matchs):
    match_number = 1
    for i in matchs:
        print(f'\n Match {match_number}:| {i.player1.first_name} \t|vs | {i.player2.first_name}\t|')
        match_number += 1


def display_opponents(player):
    for opponent in player.opponents:
        print(f'{player.first_name} a deja joue vs {opponent}')


def display_round(round_name):
    print(f'\n*********  {round_name}  *********')


def display_score(players):
    players.sort(key=lambda x: x.elo)
    players.sort(key=lambda x: x.score, reverse=True)
    print(' \n------  Score Player  ------')
    for player in players:
        print(f'| {player.first_name}  \t{player.id}\t{player.score}  |')


def display_winner(tournament_name, player):
    print(' // Tournoi termine // ')
    print(f' Le vainqueur du tournoi "{tournament_name}" est : '
          f'****************  {player}  ****************')


def display_continue_tournament():
    print(' |> Souhaitez vous continuer?')
    print(' 1 - Oui')
    print(' Q - Retour')
