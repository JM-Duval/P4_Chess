# -*-coding: utf-8 -*
# ! /usr/bin/env python
"""This file is a exercice about tinydb.
Web_site_link = https://www.docstring.fr/blog/tinydb-une-base-de-donnees-adaptee-vos-projets/"""

from model.dataBasePlayersModel import DataBasePlayers
from view.dataBasePlayersView import display_player_exist, display_player_saved, \
    display_player_delete, display_players, display_update_player, display_error_message
from model.player import Player


def enter_new_player(infos_player):
    first_name, last_name, date_birth, sexe, elo = infos_player
    new_player = Player(first_name, last_name, date_birth, sexe, elo)
    if DataBasePlayers().search(new_player) is True:
        display_player_exist(new_player)
    else:
        DataBasePlayers().insert(new_player)
        if DataBasePlayers().search(new_player) is True:
            display_player_saved(new_player)
        else:
            display_error_message()


def del_player(player):
    DataBasePlayers().remove(player)
    if DataBasePlayers().search(player) is True:
        display_error_message()
    else:
        display_player_delete(player)
        display_players(DataBasePlayers().load())


def edit_elo_player(player, new_elo):
    if DataBasePlayers().update_elo(player, new_elo) == new_elo:
        display_update_player(player, new_elo)
    else:
        display_error_message()
