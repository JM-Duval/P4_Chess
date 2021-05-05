# -*-coding: utf-8 -*
#! /usr/bin/env python
"""This file is a exercice about a program for help the chess tournament organization.
It is a first program with MVC structuring."""

import os
import glob
import sys
sys.path[:0]=['../']
from pathlib import Path

from controler.tournamentControler import TournamentControler
from model.dataBaseTournamentModel import DataTournament
from model.dataBasePlayersModel import *


path_data_tournament = Path("../data/tournaments")
path_data_players = Path("../data/list_players")
if os.path.exists(path_data_tournament):
    print ('ok')


def start_menu():
    input_start_menu = int(input('********** Menu principal **********\n'
                   '1 - Lancer un nouveau tournoi\n'
                   '2 - Reprendre un tournoi\n'
                   '3 - Enregistrer des joueurs dans la base de données\n'
                   '4 - Afficher des statistiques\n'
                   '5 - Sortir du programme\n'))
    return input_start_menu


def stat_menu():
    input_stat_menu = int(input('A - Liste des joueurs (par ordre alphabétique)\n'
           'B - Liste des joueurs (par classement)\n'
           'C - Liste des tournois\n'
           'D - Sectionner un tournoi\n'))
    return input_stat_menu


def list_tour_menu():
    print ('Selectionner un tournoi: {list_tournament}')



def tour_menu():
    input_tour_menu = int(input(('a - Liste des joueurs (par ordre alphabétique)\n'
           'b - Liste des joueurs (par classement)\n'
           'c - Liste des Rounds\n'
           'd - Liste des Matchs')))
    return input_tour_menu




def save_new_player():
    pass

def launch_new_tournament():
    pass

def restart_tournament():
    pass

def display_statistical():
    pass



#  -- Stastistiques -------------------
class DisplayPlayers:
    def __init__(self):
        self.list_players = list_players
        pass

    def sorted (self):
        # par ordre alphabétique
        # par classement
        #return sorted_list
        pass

    def display (self):
        # print (self.sorted)
        pass

class DisplayTournament:
    def __init__(self, tournament_name):
        self.tournanent_name = tournament_name
        self.list_players = list_players

    def display_players(self):
        # par ordre alphabétique
        # par classement
        # vainqueur
        pass

    def display_rounds(self):
        pass

    def display_matchs(self):
        pass

# -- Chargement des données du tournoi ---------------------------------

# -- Liste des tournois  ----------
def display_tournament_list():
    get_files_tournament = glob.glob(os.path.join(path_data_tournament, '*.json'))
    files = [os.path.basename(x) for x in get_files_tournament]

    open_tournament = []
    close_tournament = []
    for file in files:
        index = file.index('.')
        file_name = file[:index]
        if DataTournament(file_name).status() == 'open':
            open_tournament.append(file_name)
        else:
            close_tournament.append(file_name)

    print(f'\n {len(open_tournament)} tournament(s) unfinished : ')
    for file_name in open_tournament:
        print(f'  - {file_name}')

    print(f'\n {len(close_tournament)} tournament(s) finished : ')
    for file_name in close_tournament:
        print(f'  - {file_name}')


display_tournament_list()

# -- Liste des joueurs d'un tournoi -----------------------------------

def display_players_in_tournament(tournament_name, order):
    players_tour = DataTournamentPlayers(tournament_name, 'Round 1')

    if order == 1:
        print("Classement des joueurs dans l'ordre alphabetique: ")
        for i in  players_tour.sorted_alpha():
            print (f'   {i.last_name} - {i.first_name}')
    elif order == 2:
        print ('Classement des joueurs:')
        for i in players_tour.sorted_score():
            print (f'   {i.last_name} - {i.score}')
    else:
        print ('Fonction de trie pas encore disponible')


#display_players_in_tournament('Word_tour_Tournament_2', 1)
#display_players_in_tournament('Word_tour_Tournament_2', 2)


# -- Liste des joueurs inscrits dans la base -----------------------------------

def display_total_players(order):
    players = DataBasePlayers()
    #print(players.sorted_alpha())
    #print(players.sorted_elo())

    if order == 1:
        print("Classement des joueurs dans l'ordre alphabetique: ")
        for i in  players.sorted_alpha():
            print (f'   {i.last_name} - {i.first_name}')
    elif order == 2:
        print ('Classement des joueurs:')
        for i in players.sorted_elo():
            print (f'   {i.last_name} - {i.elo}')
    else:
        print ('Fonction de trie pas encore disponible')

#display_total_players(1)
#display_total_players(2)