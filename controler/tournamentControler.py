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
            self.start_time = datetime.datetime.today().strftime('%d-%m-%y at %H:%M')
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
        start_time = datetime.datetime.today().strftime('%d-%m-%y at %H:%M')
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
        self.tournament.status = 'open'
        display_start_time(self.start_time)

    def stop_tournament(self):
        self.save_tournament()

    def save_tournament(self):
        DataTournament(self.tournament_name).delete()
        DataTournament(self.tournament_name).save_tournament(self.tournament)

    def update_tour_number(self):
        self.tournament.tour_number +=1

    def close_tournament(self):
        display_winner(self.tournament_name, self.tournament.players[0].first_name)
        self.tournament.end_time = datetime.datetime.today().strftime('%d-%m-%y at %H:%M')
        self.tournament.status = "closed"
        self.save_tournament()
        display_end_time(self.tournament.end_time)

    # --  Round 1 -----------------------------------------------------
    def run_first_round(self):
        round_name = 'Round' + str(self.tournament.tour_number)
        display_round(round_name)
        self.tournament.players.sort(key=lambda x: x.elo)
        round1 = Round('Round 1')
        self.tournament.add_round(round1)
        for i in range (self.nb_match):
            round1.add_match(self.tournament.players[i],
                             self.tournament.players[i+self.nb_match])

        for match in round1.matchs: # add id player in opponent_list
            match.player1.add_opponent(match.player2.id)
            match.player2.add_opponent(match.player1.id)

        display_game_sheet('Round 1', round1.matchs)

        for i in range (self.nb_match): #add score player and save
            self._handle_score(round1.matchs[i].player1,
                               round1.matchs[i].player2)

        display_score(self.tournament.players)


    # --  Next Rounds  ---------------------------------
    def run_next_round(self):
        if self.tournament.tour_number < 4 :
            round_name = 'Round' + str(self.tournament.tour_number+1)
            display_round(round_name)
            self.tournament.players.sort(key=lambda x: x.elo)
            self.tournament.players.sort(key=lambda x: x.score, reverse=True)
            roundx = Round(round_name)
            self.tournament.add_round(roundx)
            x = 0
            for i in range(floor(len(self.checked_opponents())/2)):
                roundx.add_match(self.checked_opponents()[i+x],
                                 self.checked_opponents()[i+x+1])
                x += 1

            for match in roundx.matchs: # add id player in opponent_list
                match.player1.add_opponent(match.player2.id)
                match.player2.add_opponent(match.player1.id)

            display_score(self.tournament.players)
            display_game_sheet(round_name, roundx.matchs)

            for i in range (self.nb_match):
                self._handle_score(roundx.matchs[i].player1,
                                   roundx.matchs[i].player2)

            display_score(self.tournament.players)
            self.update_tour_number()

            if self.tournament.tour_number == 4:
                display_winner(self.tournament_name, self.tournament.players[0])

        else:
            print('Tournoi terminé')
            display_winner(self.tournament_name, self.tournament.players[0])


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