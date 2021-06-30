# -*-coding: utf-8 -*
# !/usr/bin/env python
"""This file is a exercice about a program for help the chess tournament organization.
It is a first program with MVC structuring."""

import datetime
from math import floor
from model.tournament import Tournament
from model.round import Round
from model.dataBaseTournamentModel import DataTournament
from controler.inputUserControler import UserInput
from view.tournamentView import display_start_time, display_end_time, \
    display_game_sheet, display_round, display_score, \
    display_winner, display_continue_tournament, display_update_player_now


def run_tournament(tournament_name=None, players=None):
    run = True
    while run:
        if tournament_name is None:
            players = players
            tournament_name, location, tour_number, time_control = UserInput().infos_tournament()
            start_time = None
            tournament = Tournament(tournament_name,
                                    location,
                                    start_time,
                                    tour_number,
                                    time_control)
            tour = TournamentControler(tournament, players)
            tour.start_tournament()

        else:
            tournament = DataTournament(tournament_name).load_tournament()
            players = tournament.players
            tour = TournamentControler(tournament, players)

        tour.run_round()

        if tournament.status == 'closed':
            if display_update_player_now() == '1':
                return tournament.status
                break
            else:
                break
        else:
            display_continue_tournament()
            user_input = UserInput().interval(1)
            if user_input.upper() == 'Q':
                run = False
            else:
                continue


class TournamentControler:

    def __init__(self, tournament, players):
        self.tournament = tournament
        self.tournament.players = players
        self.tournament_name = tournament.tournament_name
        self.start_time = tournament.start_time
        self.end_time = tournament.end_time
        self.nb_match = floor((len(self.tournament.players) / 2))

    def start_tournament(self):
        self.start_time = datetime.datetime.today().strftime('%d-%m-%y at %H:%M')
        self.tournament.status = 'open'
        self.save_tournament()
        display_start_time(self.start_time)

    def close_tournament(self):
        self.end_time = datetime.datetime.today().strftime('%d-%m-%y at %H:%M')
        self.tournament.status = 'closed'
        self.save_tournament()
        display_end_time(self.end_time)

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
            DataTournament(self.tournament_name).update_start_time(
                self.tournament_name, self.start_time)
            DataTournament(self.tournament_name).update_end_time(
                self.tournament_name, self.end_time)
            print('*********** Partie Sauvegardee ***********')
        else:
            DataTournament(self.tournament_name).save_tournament(self.tournament)
            print('*********** Nouvelle partie enregistree  ***********')

    def run_round(self):
        # update tour number
        self.tournament.tour_number += 1
        if self.tournament.tour_number <= 4:

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

            display_round(round_name)
            display_game_sheet(roundx.matchs)
            # update score player
            for i in range(self.nb_match):
                self._handle_score(roundx.matchs[i].player1,
                                   roundx.matchs[i].player2)

            # save file
            self.save_tournament()

            # display
            display_score(self.tournament.players)
            if self.tournament.tour_number == 4:
                display_winner(self.tournament_name, self.tournament.players[0])
                self.close_tournament()
        else:
            display_winner(self.tournament_name, self.tournament.players[0])
            self.close_tournament()

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
            while opponent_in_list is True:
                try:
                    i += 1
                    if players_sorted[i].id in players_sorted[x].opponents:
                        opponent_in_list = True
                    else:
                        opponent_list_checked.append(players_sorted[x])
                        opponent_list_checked.append(players_sorted[i])
                        players_sorted.pop(x), players_sorted.pop(i - 1)
                        opponent_in_list = False
                except IndexError:  # situation ou un joueur à déja joué vs tout le monde.
                    # il rejoue vs le joueur n+1
                    opponent_list_checked.append(players_sorted[x])
                    opponent_list_checked.append(players_sorted[x+1])
                    players_sorted.pop(x), players_sorted.pop(x)
                    break
        return opponent_list_checked

    def _handle_score(self, player1, player2):
        result_score = UserInput().score(player1, player2)
        player1.score += result_score[0]
        player2.score += result_score[1]
