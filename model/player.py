# -*-coding: utf-8 -*
#! /usr/bin/env python
"""This file is a exercice about a program for help the chess tournament organization.
It is a first program with MVC structuring."""

class Player:

    def __init__(self,first_name, score, elo, last_name='nc'):
        self.first_name = first_name
        self.last_name = last_name
        self.score = score
        self.elo = elo

    def get_name(self):
        return self.first_name

    def set_score(self, add_score):
        self.score += add_score

    def get_score(self):
        return self.score

    def __str__(self):
        out = f"name: {self.first_name}, {self.last_name} | score: {self.score} | elo: {self.elo}"
        return out


def sorted_list_players_round():
    infos_players.sort(key=lambda x: x.elo)
    infos_players.sort(key=lambda x: x.score)
    players = []
    for player in infos_players:
        players.append(player.first_name)
    return players


player1 = Player('Anna', 8, 8)  #1
player2 = Player('Eric', 22, 3) #6
player3 = Player('Sandra', 18, 4) #4
player4 = Player('Chirac', 18, 5) #5
player5 = Player('Albert', 25, 1) #8
player6 = Player('Marine', 24, 2) #7
player7 = Player('Rachel', 13, 7) #2
player8 = Player('Michel', 16, 6) #3
player9 = Player('Trump', 3, 10)
player10 = Player('Brad', 24, 13)
infos_players = [player1,player2,player3,player4,player5,player6,player7,player8, player9, player10]


def list_players():
    return infos_players


"""
def test ():
    for i in infos_players:
        print (i)
test()
"""
