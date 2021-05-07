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
from model.dataBaseTournamentModel import DataTournament, DataTournamentPlayers
from view.tournamentView import *
from view.gamesheetView import *
from view.rankingView import display_score, display_winner


class TournamentControler:

    def __init__(self, players):
        tournament_name, location, tour_number, time_control = data_input_tournament()
        self.tournament_name = tournament_name
        self.start_time = datetime.datetime.today().strftime('%d-%m-%y at %H:%M')
        self.tournament = Tournament(tournament_name,
                                     location,
                                     self.start_time,
                                     tour_number,
                                     time_control)
        self.tournament.players = players
        self.nb_match = floor((len(self.tournament.players)/2))

    def start_tournament(self):
        self.tournament.status = 'open'
        DataTournament(self.tournament_name).insert_infos_tour(self.tournament)
        display_start_time(self.start_time)

    def close_tournament(self):
        display_winner(self.tournament_name, self.tournament.players[0].first_name)
        end_time = datetime.datetime.today().strftime('%d-%m-%y at %H:%M')
        display_end_time(end_time)
        for player in self.tournament.players:
            player.clean_opponents()
        DataTournament(self.tournament_name).update("status", "closed")
        DataTournament(self.tournament_name).update("end_time", end_time)

    def save_data_round(self, round):
        DataTournament(self.tournament_name).insert_round(round)

    def update_tour_number(self):
        DataTournament(self.tournament_name).update("tour_number", self.tournament.tour_number - 1)

    # --  Round 1 -----------------------------------------------------
    def run_first_round(self, round_name):
        display_round(round_name)
        self.tournament.players.sort(key=lambda x: x.elo)
        round1 = Round('Round 1')
        #self.tournament.add_round(round1)
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
        self.save_data_round(round1)
        self.update_tour_number()

        #round1.matchs[0].score_player1, round1.matchs[0].score_player2 =
        # self.handle_score(player1, player2)

    # --  Next Rounds  ---------------------------------
    def run_next_round(self, round_name):

        display_round(round_name)
        self.tournament.players.sort(key=lambda x: x.elo)
        self.tournament.players.sort(key=lambda x: x.score, reverse=True)
        roundx = Round(round_name)
        #self.tournament.add_round(roundx)
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
        self.save_data_round(roundx)
        self.update_tour_number()


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