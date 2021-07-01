# -*-coding: utf-8 -*
# !/usr/bin/env python
"""This file is a exercice about tinydb.
Web_site_link = https://www.docstring.fr/blog/tinydb-une-base-de-donnees-adaptee-vos-projets/"""

from tinydb import TinyDB, Query
from model.tournament import Tournament
from model.round import Round
from model.player import Player
import os


class DataTournament:
    def __init__(self, tournament_name=None):
        self.tournament_name = tournament_name
        self.name_table = "tournament"
        self.name_file = "tournaments.json"
        path_data_tournament = "data/tournaments"
        db = TinyDB(os.path.join(path_data_tournament, self.name_file))
        self.tournament_table = db.table(self.name_table)

    def serialized_tournament(self, tournament):
        serialized_tournament = {
            "tournament_name": tournament.tournament_name,
            "start_time": tournament.start_time,
            "tour_number": tournament.tour_number,
            "location": tournament.location,
            "time_control": tournament.time_control,
            "status": tournament.status,
            "end_time": tournament.end_time,
            "players": [
                self._serialized_player(player) for player in tournament.players
            ],
            "rounds": [
                self._serialized_round(round, round.round_name)
                for round in tournament.rounds
            ],
        }
        return serialized_tournament

    def _serialized_round(self, round, round_name):
        serialized_round = {
            round_name: [self._serialized_match(match) for match in round.matchs]
        }
        return serialized_round

    def _serialized_match(self, match):
        serialized_match = {
            "match": (
                self._serialized_player(match.player1),
                self._serialized_player(match.player2),
            )
        }
        return serialized_match

    def _serialized_player(self, player):
        serialized_player = {
            "first_name": player.first_name,
            "last_name": player.last_name,
            "date_birth": player.date_birth,
            "sexe": player.sexe,
            "elo": player.elo,
            "id": player.id,
            "score": player.score,
            "opponents": player.opponents,
        }
        return serialized_player

    def _deserialized_tournament(self, serialized_tournament):
        tournament_name = serialized_tournament["tournament_name"]
        start_time = serialized_tournament["start_time"]
        tour_number = serialized_tournament["tour_number"]
        location = serialized_tournament["location"]
        time_control = serialized_tournament["time_control"]
        status = serialized_tournament["status"]
        end_time = serialized_tournament["end_time"]
        players = [
            self._deserialized_player(player)
            for player in serialized_tournament["players"]
        ]
        rounds = [
            self._deserialized_round(round) for round in serialized_tournament["rounds"]
        ]
        tournament = Tournament(
            tournament_name=tournament_name,
            start_time=start_time,
            tour_number=tour_number,
            location=location,
            time_control=time_control,
            status=status,
            end_time=end_time,
        )
        tournament.players = players
        tournament.rounds = rounds
        return tournament

    def _deserialized_round(self, serialized_round):
        for round_name, match in serialized_round.items():
            round = Round(round_name)
            for i in range(len(match)):
                player1 = match[i]["match"][0]
                player2 = match[i]["match"][1]
                round.add_match(
                    self._deserialized_player(player1),
                    self._deserialized_player(player2),
                )
            return round

    def _deserialized_player(self, serialized_player):
        first_name = serialized_player["first_name"]
        last_name = serialized_player["last_name"]
        date_birth = serialized_player["date_birth"]
        sexe = serialized_player["sexe"]
        elo = serialized_player["elo"]
        id = serialized_player["id"]
        score = serialized_player["score"]
        opponents = serialized_player["opponents"]
        player = Player(
            first_name=first_name,
            last_name=last_name,
            date_birth=date_birth,
            sexe=sexe,
            elo=elo,
            score=score,
        )
        player.id = id
        player.opponents = opponents
        return player

    def save_tournament(self, tournament):
        self.tournament_table.insert(self.serialized_tournament(tournament))

    def load_tournament(self):
        Tour = Query()
        serialized_tournament = self.tournament_table.search(
            Tour.tournament_name == self.tournament_name
        )
        tournament = self._deserialized_tournament(serialized_tournament[0])
        return tournament

    def update_data_players(self, tournament_name, players):
        Tour = Query()
        self.tournament_table.upsert(
            {
                "tournament_name": tournament_name,
                "players": [self._serialized_player(player) for player in players],
            },
            Tour.tournament_name == tournament_name,
        )

    def update_rounds(self, tournament_name, rounds):
        Tour = Query()
        self.tournament_table.upsert(
            {
                "tournament_name": tournament_name,
                "rounds": [
                    self._serialized_round(round, round.round_name) for round in rounds
                ],
            },
            Tour.tournament_name == tournament_name,
        )

    def update_tour_number(self, tournament_name, tour_number):
        Tour = Query()
        self.tournament_table.upsert(
            {"tournament_name": tournament_name, "tour_number": tour_number},
            Tour.tournament_name == tournament_name,
        )

    def update_status(self, tournament_name, status):
        Tour = Query()
        self.tournament_table.upsert(
            {"tournament_name": tournament_name, "status": status},
            Tour.tournament_name == tournament_name,
        )

    def update_start_time(self, tournament_name, start_time):
        Tour = Query()
        self.tournament_table.upsert(
            {"tournament_name": tournament_name, "start_time": start_time},
            Tour.tournament_name == tournament_name,
        )

    def update_end_time(self, tournament_name, end_time):
        Tour = Query()
        self.tournament_table.upsert(
            {"tournament_name": tournament_name, "end_time": end_time},
            Tour.tournament_name == tournament_name,
        )

    def exist(self, tournament_name):
        Tour = Query()
        if (
            len(self.tournament_table.search(Tour.tournament_name == tournament_name))
            != 0
        ):
            return True
        else:
            return False

    def insert(self, new_tournament):
        self.tournament_table.insert(self.serialized_tournament(new_tournament))

    def get_rounds(self):
        return [
            self.load_tournament().rounds[i].round_name
            for i in range(len(self.load_tournament().rounds))
        ]

    def get_matchs(self):
        matchs = []
        for round in self.load_tournament().rounds:
            [matchs.append(players) for players in round.matchs]
        return matchs

    def get_infos_tour(self):
        tour = self.load_tournament()
        return (
            tour.tournament_name,
            tour.location,
            tour.start_time,
            tour.end_time,
            tour.tour_number,
            tour.status,
            self.get_sorted_players_score(),
        )

    def get_sorted_players_alpha(self):
        return sorted(self.load_tournament().players, key=lambda x: x.last_name)

    def get_sorted_players_score(self):
        return sorted(
            self.load_tournament().players, key=lambda x: x.score, reverse=True
        )


class AllTournaments:
    def __init__(self):
        self.name_table = "tournament"
        self.name_file = "tournaments.json"
        path_data_tournament = "data/tournaments"
        db = TinyDB(os.path.join(path_data_tournament, self.name_file))
        self.tournament_table = db.table(self.name_table)

    def list(self):
        list_tournaments = []
        [
            list_tournaments.append(tour["tournament_name"])
            for tour in self.tournament_table.all()
        ]
        return list_tournaments

    def status_open(self):
        list_tournaments_open = []
        for tour in self.tournament_table.all():
            if tour["status"] == "open":
                list_tournaments_open.append(tour["tournament_name"])
        return list_tournaments_open

    def status_close(self):
        list_tournaments_closed = []
        for tour in self.tournament_table.all():
            if tour["status"] == "close":
                list_tournaments_closed.append(tour)
        return list_tournaments_closed
