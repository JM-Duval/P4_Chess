# -*-coding: utf-8 -*
# ! /usr/bin/env python
"""This file is a exercice about tinydb.
Web_site_link = https://www.docstring.fr/blog/tinydb-une-base-de-donnees-adaptee-vos-projets/"""

from model.player import Player
from tinydb import TinyDB, Query
import os
import sys
sys.path[:0] = ["../"]


class DataBasePlayers:
    def __init__(self):
        self.name_table = "players"
        self.name_file = "players_chess.json"
        origin_path = sys.path[(len(sys.path)) - 2][:-4]
        path_data_players = os.path.join(origin_path, "data/list_players")
        db = TinyDB(os.path.join(path_data_players, self.name_file))
        self.players_table = db.table(self.name_table)

    def search(self, player):
        Person = Query()
        if (
            self.players_table.search(Person.last_name == player.last_name)
            and self.players_table.search(Person.first_name == player.first_name)
            and self.players_table.search(Person.date_birth == player.date_birth)
        ):
            return True
        else:
            return False

    def _serialized(self, player):
        serialized_player = {
            "first_name": player.first_name,
            "last_name": player.last_name,
            "date_birth": player.date_birth,
            "sexe": player.sexe,
            "elo": player.elo,
        }
        return serialized_player

    def _deserialized(self, serialized_players):
        players = []

        def _deserialized_step(serialized_player):
            first_name = serialized_player["first_name"]
            last_name = serialized_player["last_name"]
            date_birth = serialized_player["date_birth"]
            sexe = serialized_player["sexe"]
            elo = serialized_player["elo"]
            player = Player(
                first_name=first_name,
                last_name=last_name,
                date_birth=date_birth,
                sexe=sexe,
                elo=elo,
            )
            players.append(player)

        for serialized_player in serialized_players:
            _deserialized_step(serialized_player)
        return players

    def insert(self, player):
        if self.search(player) is True:
            return False
        else:
            print(self.players_table.insert(self._serialized(player)))
            return True

    def load(self):
        serialized_players = self.players_table.all()
        return self._deserialized(serialized_players)

    def remove(self, player):
        Person = Query()
        self.players_table.remove(
            Person.last_name == player.last_name, Person.elo == player.elo
        )

    def update(self, player, arg, new_value):
        Person = Query()
        self.players_table.update({arg: +new_value}, Person["last_name"] == player)

    def sorted_alpha(self):
        return sorted(self.load(), key=lambda x: x.last_name)

    def sorted_elo(self):
        return sorted(self.load(), key=lambda x: x.elo)

    def exist(self, player):
        Player = Query()
        print(player.id)
        if len(self.players_table.search(Player.id == player.id)) != 0:
            return True
        else:
            return False

    def update_elo(self, player, new_elo):
        Person = Query()
        self.players_table.update({'elo': new_elo}, Person['last_name'] == player.last_name)
        return self.players_table.search(Person['last_name'] == player.last_name)[0]['elo']
