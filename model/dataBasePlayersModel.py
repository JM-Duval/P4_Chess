# -*-coding: utf-8 -*
#! /usr/bin/env python
"""This file is a exercice about tinydb.
Web_site_link = https://www.docstring.fr/blog/tinydb-une-base-de-donnees-adaptee-vos-projets/"""

from tinydb import TinyDB, Query, where
# TinyDB is the database
# Query allows to query the data base
# where allows to refine the search

class DataBasePlayers:
    def __init__(self):
        self.name_table = 'players'
        self.name_file = 'players_chess.json'
        db = TinyDB(self.name_file)
        self.players_table = db.table(self.name_table)

    def search(self, player):
        Person = Query()
        if self.players_table.search(Person.last_name == player):
            return True
        else:
            return False

    def _serialized(self, player):
        serialized_player = {
        'first_name' : player.first_name,
        'last_name' : player.last_name,
        'date_birth' : player.date_birth,
        'sexe' : player.sexe,
        'elo' : player.elo
        }
        return serialized_player

    def _deserialized(self, serialized_players):
        players = []
        def _deserialized_step(serialized_player):
            first_name = serialized_player['first_name']
            last_name = serialized_player['last_name']
            date_birth = serialized_player['date_birth']
            sexe = serialized_player['sexe']
            elo = serialized_player['elo']
            player = Player(first_name=first_name, last_name=last_name,
                            date_birth=date_birth, sexe=sexe, elo=elo
                            )
            players.append(player)
        for serialized_player in serialized_players:
            _deserialized_step(serialized_player)
        return players

    def insert(self, player):
        if self.search(player.last_name):
            print (f"{player.first_name}.{player.last_name} "
                   f"existe deja dans la liste" )
        else:
            self.players_table.insert(self._serialized(player))
            print (f"{player.first_name}.{player.last_name} à été ajouté" )
            self.display()

    def load(self):
        serialized_players = self.players_table.all()
        return self._deserialized(serialized_players)

    def remove(self, player):
        if self.search(player):
            Person = Query()
            self.players_table.remove(Person.last_name == player)
            print (f'{player} à été supprimé')
            self.display()
        else:
            print (f"{player} n'existe pas dans la liste" )

    def update(self, player, arg, new_value):
        if self.search(player):
            Person = Query()
            self.players_table.update({arg: new_value}, Person.last_name == player)
            print (f'{player} a maintenant {new_value}')
            self.display()
        else:
            print (f"{player} n'existe pas dans la liste" )

    def display(self):
        for i in self.load():
            return i.__dict__

    def get(self, *args):
        for i in self.load():
            for arg in args:
                print (i.__dict__[arg])