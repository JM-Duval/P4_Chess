# -*-coding: utf-8 -*
#! /usr/bin/env python
"""This file is a exercice about a program for help the chess tournament organization.
It is a first program with MVC structuring."""


# -- Classement --
def print_score(players):
    players.sort(key=lambda x: x.elo)
    players.sort(key=lambda x: x.score, reverse=True)
    print (f' --  Score player  -- \n')
    for player in players:
        print (f'| {player.first_name} ({player.id}) : {player.score} |')