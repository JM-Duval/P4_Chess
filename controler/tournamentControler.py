# -*-coding: utf-8 -*
#! /usr/bin/env python
"""This file is a exercice about a program for help the chess tournament organization.
It is a first program with MVC structuring."""

from math import floor
import datetime
import sys
sys.path[:0]=['../']
from model.tournament import Tournament
from model.round import Round
from model.match import Match
from model.player import Player
from model.dataBaseTournamentModel import DataTournament #, DataTournamentPlayers
from view.tournamentView import *
from view.gamesheetView import *
from view.rankingView import display_score, display_winner


class TournamentControler:

    def __init__(self, players, tournament = None):

        if tournament == None:
            tournament_name, location, start_time, tour_number, time_control = self.new_tournament()
            self.tournament_name = tournament_name
            #self.start_time = datetime.datetime.today().strftime('%d-%m-%y at %H:%M')
            self.start_time = None
            self.tour_number = tour_number
            self.tournament = Tournament(tournament_name,
                                         location,
                                         start_time,
                                         tour_number,
                                         time_control)
            self.tournament.players = players

        else:
            tournament_name, location, start_time, end_time, tour_number, \
            time_control, players, rounds, description, status =self.restart_tournament(tournament)
            self.tournament_name = tournament_name
            self.tour_number = tour_number
            self.tournament = Tournament(tournament_name,
                                         location,
                                         start_time,
                                         tour_number,
                                         time_control,
                                         status)
            self.tournament.players = players
            self.tournament.rounds = rounds

        self.nb_match = floor((len(self.tournament.players) / 2))

    def new_tournament(self):
        tournament_name, location, tour_number, time_control = data_input_tournament()
        #start_time = datetime.datetime.today().strftime('%d-%m-%y at %H:%M')
        start_time = None
        return tournament_name, location, start_time, tour_number, time_control

    def restart_tournament(self, tournament):
        tournament_name = tournament.tournament_name
        location = tournament.location
        start_time = tournament.start_time
        end_time = tournament.end_time
        tour_number = tournament.tour_number
        time_control = tournament.time_control
        players = tournament.players
        rounds = tournament.rounds
        description = tournament.description
        status = tournament.status
        return tournament_name, location, start_time, end_time, tour_number,\
               time_control, players, rounds, description, status


    def start_tournament(self):
        self.start_time = datetime.datetime.today().strftime('%d-%m-%y at %H:%M')
        self.tournament.status = 'open'
        self.save_tournament()
        display_start_time(self.start_time)

    def close_tournament(self):
        self.tournament.end_time = datetime.datetime.today().strftime('%d-%m-%y at %H:%M')
        self.tournament.status = 'closed'
        self.save_tournament()
        display_end_time(self.tournament.end_time)

    def save_tournament(self):
        if DataTournament().exist(self.tournament_name):
            DataTournament(self.tournament_name).update_tour_number(
                self.tournament_name, self.tournament.tour_number)
            DataTournament(self.tournament_name).update_data_players(
                self.tournament_name, self.tournament.players)
            DataTournament(self.tournament_name).update_rounds(
                self.tournament_name, self.tournament.rounds)
            DataTournament(self.tournament_name).update_status(
                self.tournament_name, self.tournament.status)
            print('*********** Partie Sauvegardee ***********')
        else:
            DataTournament(self.tournament_name).save_tournament(self.tournament)
            print('*********** Nouvelle partie enregistree  ***********')


    # -- Rounds  ---------------------------------------
    def run_round(self):
        # update tour number
        self.tournament.tour_number += 1
        if self.tournament.tour_number <= 4 :

            # sorted players
            self.sorted_players(self.tournament.tour_number)

            # build round
            round_name = 'Round' + str(self.tournament.tour_number)
            roundx = Round(round_name)
            self.tournament.add_round(roundx)
            x = 0
            for i in range(floor(len(self.checked_opponents())/2)):
                roundx.add_match(self.checked_opponents()[i+x],
                                 self.checked_opponents()[i+x+1])
                x += 1

            # add id player in opponent_list
            for match in roundx.matchs:
                match.player1.add_opponent(match.player2.id)
                match.player2.add_opponent(match.player1.id)

            # update score player
            for i in range (self.nb_match):
                self._handle_score(roundx.matchs[i].player1,
                                   roundx.matchs[i].player2)

            # save file
            self.save_tournament()

            # display
            display_round(round_name)
            display_game_sheet(roundx.matchs)
            display_score(self.tournament.players)
            if self.tournament.tour_number == 4:
                display_winner(self.tournament_name, self.tournament.players[0])

        else:
            display_winner(self.tournament_name, self.tournament.players[0])


    def sorted_players(self, tour_number):
        if tour_number == 1:
            self.tournament.players.sort(key=lambda x: x.elo)
        else:
            self.tournament.players.sort(key=lambda x: x.elo)
            self.tournament.players.sort(key=lambda x: x.score, reverse=True)

    def checked_opponents(self):
        players_sorted = []
        for i in self.tournament.players:
            players_sorted.append(i)
        opponent_list_checked = []
        while len(players_sorted) > 1:
            x = 0
            i = x
            opponent_in_list = True
            while opponent_in_list:
                try:
                    i += 1
                    if players_sorted[i].id in players_sorted[x].opponents:
                        opponent_in_list = True
                    else:
                        opponent_list_checked.append(players_sorted[x])
                        opponent_list_checked.append(players_sorted[i])
                        players_sorted.pop(x), players_sorted.pop(i - 1)
                        opponent_in_list = False
                except:  # situation ou un joueur à déja joué vs tout le monde.
                    # il rejoue vs le joueur n+1
                    opponent_list_checked.append(players_sorted[x])
                    opponent_list_checked.append(players_sorted[x+1])
                    players_sorted.pop(x), players_sorted.pop(x)
                    break
        return opponent_list_checked

    def _handle_score(self, player1, player2):
        result_score = enter_score(player1, player2)
        player1.score += result_score[0]
        player2.score += result_score[1]
