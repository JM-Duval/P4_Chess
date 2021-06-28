# -*-coding: utf-8 -*
# ! /usr/bin/env python
"""This file is a exercice about tinydb.
Web_site_link = https://www.docstring.fr/blog/tinydb-une-base-de-donnees-adaptee-vos-projets/"""


def display_player_exist(player):
    print(f'{player.last_name} est deja inscrit.')


def display_player_saved(player):
    print(f'{player.last_name} a ete enregistre.')


def display_player_delete(player):
    print(f'{player} a ete supprime(e).')


def display_players(players):
    x = 1
    for player in players:
        print(f'{x} - {player}  -  elo : {player.elo}')
        x += 1
