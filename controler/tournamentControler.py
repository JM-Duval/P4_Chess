# -*-coding: utf-8 -*
#! /usr/bin/env python
"""This file is a exercice about a program for help the chess tournament organization.
It is a first program with MVC structuring."""

from math import floor
import tournament as model_tournament
import round as model_round
import match as model_match
import player as model_player


# -- data ----------------------------------------
new_tournament = model_tournament.Tournament
rounds = new_tournament.create_tournament()
#print (tournoi)

#b = model_round.Round('Rounds 1 :')
#round = b.create_round()
#print ('Round : ', round)

#c = model_match.Match('Player 1', 'Player 2')
#match = c.create_match()
#print (match)


# -- sorted_list ---------------------------------
list_players = model_player.list_players()

def sorted_list_players():
    list_players.sort(key=lambda x: x.elo)
    list_players.sort(key=lambda x: x.score, reverse = True)
    players = []
    for player in list_players:
        players.append(player)
    return players

nb_match = floor(len(sorted_list_players())/2)


# -- Round_1 -------------------------------------
def create_round_1():
    r1 = model_round.Round(rounds[0], nb_match)
    round1 = r1.create_round()
    for i in range (nb_match):
        match = model_match.Match(sorted_list_players()[i], sorted_list_players()[nb_match + i])
        infos_match = match.create_match()
        round1.append(infos_match)
        i +=1
    return round1

y = 1
for i in create_round_1():
    print (f'Round-1 Match{y} : {i}')
    y+=1















""""
round1 = []
for i in range(nb_match):
    match = []
    match.append(sorted_list_players()[i])
    match.append((sorted_list_players()[nb_match+i]))
    #print (match)
    round1.append(match)

print ('Round 1',round1)


# -- Create list A & B --


def create_list_a():
    list_player = sorted_list_players()
    list_player_a = []
    list_player_b = []
    y = 0
    while y < floor(len(sorted_list_players())/2):
        list_player_a.append(list_player[y])
        y += 1
    print ('liste A :',list_player_a)

create_list_a()

def create_list_b():
    list_player = sorted_list_players()
    list_player_b = []
    y = floor(len(sorted_list_players())/2)
    z = y*2
    while y < z :
        list_player_b.append(list_player[y])
        y += 1
    print ('liste B :', list_player_b)
    return list_player_b

create_list_b()





def launch_tournament():
    round = []
    for i in tournoi:
        r = modele_rounds.Round(i)
        r.create_round()
        round.append(r)
    return round

launch_tournament()

list_name_players = []
    for i in infos_players:
        list_name_players.append(i.name)
    #print(list_name_players)

def sorted_list_players_round():
    infos_players.sort(key=lambda x: x.elo)
    infos_players.sort(key=lambda x: x.score)
    players = []
    for player in infos_players:
        players.append(player.name)
    return players



Etape 1 : récupérer la liste des joueurs
            trier la liste des jouers
            Créer le tournoi
            créer les rounds
            créer les matchs
            insérer les joueurs dans les matchs"""










"""

list_player = modele_players.player()
sorted_list_players_round = modele_players.sorted_list_players_round()



def nombre_match():
    nb_match = floor(len(list_player) / 2)
    return nb_match

def create_matchs():
    list_a = create_list_a()
    list_b = create_list_b()
    y = 0
    for match in range (nombre_match()):
        player_match = []
        player_match.append(list_a[y])
        player_match.append(list_b[y])
        #print (f'match{y} : ', player_match)
        print (player_match[0])
        print (player_match[1])
        y +=1

"""


