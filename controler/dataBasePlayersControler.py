# -*-coding: utf-8 -*
# ! /usr/bin/env python
"""This file is a exercice about tinydb.
Web_site_link = https://www.docstring.fr/blog/tinydb-une-base-de-donnees-adaptee-vos-projets/"""

from model.dataBasePlayersModel import DataBasePlayers
from view.dataBasePlayersView import display_player_exist, display_player_saved, \
    display_player_delete, display_players
from model.player import Player
import sys
sys.path[:0] = ['../']


player1 = ('annie', 'cordy', '16/06/1928', 'women', 8)
player2 = ('Eric', 'Zemmour', '31/08/1958', 'm', 3)
player3 = ('Jennifer', 'Lopez', '24/07/1969', 'w', 4)
player4 = ('Jacques', 'Chirac', '29/11/1932', 'm', 5)
player5 = ('Albert', 'Einstein', '14/03/1879', 'm', 1)
player6 = ('Elycia', 'Marie',  '30/03/1986', 'w', 2)
player7 = ('Rachel', 'McAdams', '17/11/1978', 'w', 7)
player8 = ('Arnold', 'Schwarzenegger', '30/07/1947', 'm', 6)
player9 = ('Donald', 'Trump', '14/06/1946', 'm', 10)
player10 = ('Brad', 'Pitt', '18/12/1963', 'm', 13)
# players = [player1,player2,player3,player4,player5,player6,player7,player8]

player_Rins = ('Alex', 'Rins', '25', 'Man', 9)
player_Martin = ('Jorge', 'Martin', '23', 'Man', 13)
player_Mir = ('Joan', 'Mir', '23', 'Man', 4)
player_Rossi = ('Valentino', 'Rossi', '42', 'Man', 21)
player_Miller = ('Jack', 'Miller', '26', 'Man', 6)
player_Marquez = ('Marc', 'Marquez', '28', 'Man', 15)
player_Zarco = ('Johan', 'Zarco', '30', 'Man', 5)
player_Morbidelli = ('Franco', 'Morbidelli', '26', 'Man', 8)
players = [player_Rins, player_Martin, player_Mir, player_Rossi, player_Miller,
           player_Marquez, player_Zarco, player_Morbidelli, player1, player2,
           player3, player4, player5, player6, player7, player8]


def enter_new_player(infos_player):
    first_name, last_name, date_birth, sexe, elo = infos_player
    new_player = Player(first_name, last_name, date_birth, sexe, elo)
    if DataBasePlayers().search(new_player) is True:
        display_player_exist(new_player)
    else:
        DataBasePlayers().insert(new_player)
        if DataBasePlayers().search(new_player) is True:
            display_player_saved(new_player)


def del_player(player):
    DataBasePlayers().remove(player)
    if DataBasePlayers().search(player) is True:
        print('probleme')
    else:
        display_player_delete(player)
        display_players(DataBasePlayers().load())


def edit_player():
    print('Fonction non disponible pour le moment')
