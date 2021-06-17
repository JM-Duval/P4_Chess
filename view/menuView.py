# -*-coding: utf-8 -*
#! /usr/bin/env python
"""This file is a exercice about a program for help the chess tournament organization.
It is a first program with MVC structuring."""

import os
import sys
sys.path[:0]=['../']


def display_home_menu():
    print()
    print("   * Menu Principal * ")
    print()
    print(" 1 - Commencer un nouveau tournoi")
    print(" 2 - Reprendre un tournoi")
    print(" 3 - Enregistrer des joueurs dans la base de donnees")
    print(" 4 - Afficher les rapports et statistiques des tournois")
    print(" Q - Quitter le programme")
    os.system('clear')

def display_statistics_menu():
    print()
    print(" * Statistiques menu 1 *")
    print()
    print(" 1 - Classement general des joueurs par ordre alphabetique")
    print(" 2 - Classement general des joueurs par score")
    print(" 3 - Liste des tournois")
    print(" Q - Retour au menu precedent")

def display_statistics_tournament_menu():
    print()
    print(f" * Statistiques menu 2  *")
    print()
    print(" 1 - Classement des joueurs par ordre alphabetique")
    print(" 2 - Classement des joueurs par score")
    print(" 3 - Visualiser les rounds")
    print(" 4 - Visualiser les matchs")
    print(" Q - Retour au menu precedent")


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


def display_list_tournaments(tournaments):
    print()
    print(" * Liste des tournois *")
    print()
    for i in range(len(tournaments)):
        print(f" {i+1} - {tournaments[i]}")
    print (" Q - Retour au menu precedent")
    return len(tournaments)


class Display:
    def __init__(self):
        pass

    def players(self, players):
        print('\n - Liste des joueurs triee : ')
        for player in players:
            print(player)

    def tournaments(self, tournaments):
        print('Liste des Tournois : ')
        for tournament_name in tournaments:
            print(tournament_name)

    def select_tournament(self, tournaments):
        x = 1
        print(f' Selectionner un tournoi ci dessous : ')
        for tournament_name in tournaments:
            print(f'{tournament_name} enter {x}')
            x+=1
        select_tournament = int(input(' >>> '))
        return select_tournament

    def matchs(self, matchs):
        print(' - Liste des Matchs : \n')
        for match in matchs:
            print(match)

    def rounds(self, rounds):
        print(' - Liste des Rounds : \n')
        for round in rounds:
            print(round)








"""
    def main_menu(self):
        input_main_menu = int(input('********** Menu principal **********\n'
                                     '1 - Lancer un nouveau tournoi\n'
                                     '2 - Reprendre un tournoi\n'
                                     '3 - Enregistrer des joueurs dans la base de données\n'
                                     '4 - Afficher des statistiques\n'
                                     '5 - Sortir du programme\n'
                                     ' >>> '))
        return input_main_menu

    def statistics_menu(self):
        input_statistics_menu = int(input('***** Menu Statistiques *****\n'
            '1 - Classement général des joueurs par ordre alphabétique\n'
            '2 - Classement général des joueurs par score\n'
            '3 - Liste des tournois\n'
            '4 - Visualiser un tournoi\n'
            '5 - Retour\n'
            ' >>> ')
        )
        return input_statistics_menu

    def statistics_menu_2(self):
        input_statistics_menu_2 = int(input(
            '1 - Classement des joueurs par ordre alphabétique\n'
            '2 - Classement des joueurs par score\n'
            '3 - Visualiser les rounds\n'
            '4 - Visualiser les matchs\n'
            '5 - Retour\n'
            ' >>> ')
        )
        return input_statistics_menu_2
"""