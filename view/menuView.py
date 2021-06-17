# -*-coding: utf-8 -*
#! /usr/bin/env python
"""This file is a exercice about a program for help the chess tournament organization.
It is a first program with MVC structuring."""

import os
import sys
sys.path[:0]=['../']


def display_main_menu():
    print()
    print("   * Menu Principal * ")
    print()
    print(" 1 - Commencer un nouveau tournoi")
    print(" 2 - Reprendre un tournoi")
    print(" 3 - Enregistrer des joueurs dans la base de donnees")
    print(" 4 - Afficher les rapports et statistiques")
    print(" Q - Quitter le programme")
    os.system('clear')

def display_statistics_menu():
    print()
    print(" * Rapports & Statistiques *")
    print()
    print(" 1 - Classement general des joueurs par ordre alphabetique")
    print(" 2 - Classement general des joueurs par score")
    print(" 3 - Liste des tournois")
    print(" Q - Retour au menu precedent")
    os.system('clear')


def display_list_tournaments(tournaments):
    print()
    print(" * Liste des tournois *")
    print()
    for i in range(len(tournaments)):
        print(f" {i+1} - {tournaments[i]}")
    print (" Q - Retour au menu precedent")
    return len(tournaments)


def display_statistics_tournament_menu(tournament_name):
    print()
    print(f" * Rapports & Statistiques du {tournament_name}  *")
    print()
    print(" 1 - Classement des joueurs par ordre alphabetique")
    print(" 2 - Classement des joueurs par score")
    print(" 3 - Visualiser les rounds")
    print(" 4 - Visualiser les matchs")
    print(" Q - Retour au menu precedent")
    os.system('clear')


def user_input(range):
    while True:
        input_user = input(" Selectionnez votre option >>>  : ")
        try:
            if int(input_user) <=range :
                break
            else:
                print(f'Selectionnez un nombre < ou = à {range}')
        except ValueError:
            if input_user.upper() == 'Q':
                break
            else:
                print("Oops! Saisie incorrect. Essayez à nouveau...")
    return input_user


def display_players(players):
    """
    print('\n - Liste des joueurs triee : ')
    for player in players:
        print(player)
    """
    os.system('clear')
    print(' |> Liste des joueurs : ')
    x=1
    for player in players:
        print(
            f"  {x}  - {player.first_name} {player.last_name}\t elo - {player.elo}")
        x += 1

def display_tournaments(tournaments):
    print(' |> Liste des Tournois : ')
    for tournament_name in tournaments:
        print(tournament_name)

def display_select_tournament(tournaments):
    x = 1
    print(f' |> Selectionner un tournoi ci dessous : ')
    for tournament_name in tournaments:
        print(f'{tournament_name} enter {x}')
        x+=1
    select_tournament = int(input(' >>> '))
    return select_tournament

def display_matchs(matchs):
    print(' |> Liste des Matchs : \n')
    for match in matchs:
        print(match)

def display_rounds(rounds):
    print(' |> Liste des Rounds : \n')
    for round in rounds:
        print(round)

def display_title_select_players():
    print(' |> Selectionnez vos 8 joueurs : \n')

def display_selected_player_fail():
    print(' |> Joueur deja selectionne')

