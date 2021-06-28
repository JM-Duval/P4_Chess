# -*-coding: utf-8 -*
# ! /usr/bin/env python
"""This file is a exercice about a program for help the chess tournament organization.
It is a first program with MVC structuring."""

import os
import sys
sys.path[:0] = ['../']


class DisplayMenu:
    def __init__(self):
        pass

    def main(self):
        print()
        print("   * Menu Principal * ")
        print()
        print(" 1 - Commencer un nouveau tournoi")
        print(" 2 - Reprendre un tournoi")
        print(" 3 - Acceder a la base de donnees des joueurs")
        print(" 4 - Afficher les rapports et statistiques")
        print(" Q - Quitter le programme")
        os.system('clear')

    def statistics(self):
        print()
        print(" * Rapports & Statistiques *")
        print()
        print(" 1 - Classement des joueurs par ordre alphabetique")
        print(" 2 - Classement general")
        print(" 3 - Liste des tournois")
        print(" Q - Retour au menu precedent")
        os.system('clear')

    def statistics_tournament(self, tournament_name):
        print()
        print(f" * Rapports & Statistiques du {tournament_name}  *")
        print()
        print(" 1 - Details du tournoi")
        print(" 2 - Classement des joueurs par ordre alphabetique")
        print(" 3 - Classement des joueurs par score")
        print(" 4 - Visualiser les rounds")
        print(" 5 - Visualiser les matchs")
        print(" Q - Retour au menu precedent")
        os.system('clear')

    def statistics_players(self):
        print()
        print(" * Base de donnees joueurs *")
        print()
        print(" 1 - Afficher les joueurs")
        print(" 2 - Enregistrer un nouveau joueur ")
        print(" 3 - Modifier les donnees d un joueur ")
        print(" 4 - Supprimer un joueur")
        print()
        os.system('clear')


class DisplayList:
    def __init__(self):
        pass

    def tournaments(self, tournaments):
        print()
        print(" * Liste des tournois *")
        print()
        for i in range(len(tournaments)):
            print(f" {i+1} - {tournaments[i]}")
        print(" Q - Retour au menu precedent")
        return len(tournaments)

    def rounds(self, rounds):
        print(' |> Liste des Rounds : \n')
        for round in rounds:
            print(round)

    def matchs(self, matchs):
        print(' |> Liste des Matchs : \n')
        for match in matchs:
            print(f'{match}')

    def players(self, players):
        x = 1
        for player in players:
            print(
                f"  {x}  - {player.first_name} {player.last_name}\t elo - {player.elo}")
            x += 1

    def score_players(self, players):
        x = 1
        for player in players:
            print(
                f"  {x}  - {player.first_name} {player.last_name}\t score - {player.score}")
            x += 1

    def player(self, player):
        print(f"  - {player.first_name} {player.last_name}\t elo - {player.elo}")

    def infos_tour(self, infos_tour):
        tournament_name, location, start_time, end_time, tour_number, status, players = infos_tour
        print(f'- Nom : {tournament_name}')
        print(f'- Localisation : {location}')
        print(f'- Date de début : {start_time}')
        print(f'- Date de fin : {end_time}')
        print(f'- Nombre de rounds joue : {tour_number}')
        print(f'- Statut : {status}')
        print('- Joueurs:')
        self.score_players(players)
        input('')


class DisplayMessage:
    def __init__(self):
        pass

    def list_tournaments(self):
        print(' |> Liste des Tournois : ')

    def list_players(self):
        print('Liste des joueurs:')

    def select_tournament(self):
        print(' |> Selectionner un tournoi ci dessous : ')

    def no_tournament(self):
        print('Tous les tournois sont termines.')

    def select_players(self):
        print(' |> Selectionnez vos 8 joueurs : \n')

    def selected_players(self):
        print('Liste des joueurs selectionnes:')

    def player_error(self, player):
        print(f' {player} est deja inscrit.')


def display_continue():
    print(' |> Souhaitez vous continuer?')
    print(' 1 - Oui')
    print(' Q - Retour')



