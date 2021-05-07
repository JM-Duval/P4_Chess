# -*-coding: utf-8 -*
#! /usr/bin/env python
"""This file is a exercice about a program for help the chess tournament organization.
It is a first program with MVC structuring."""

import sys
sys.path[:0]=['../']
from controler.tournamentControler import TournamentControler
from model.dataBaseTournamentModel import DataTournament
from model.player import Player

player1 = Player('Annie', 'Cordy', '16/06/1928', 'w', 8)  #9
player2 = Player('Eric', 'Zemmour', '31/08/1958', 'm', 3) #4
player3 = Player('Jennifer', 'Lopez', '24/07/1969', 'w' , 4) #6
player4 = Player('Jacques', 'Chirac', '29/11/1932', 'm' , 5) #5
player5 = Player('Albert', 'Einstein', '14/03/1879', 'm', 1) #1
player6 = Player('Elycia', 'Marie',  '30/03/1986', 'w' , 2) #2
player7 = Player('Rachel', 'McAdams', '17/11/1978', 'w', 7) #8
player8 = Player('Arnold', 'Schwarzenegger', '30/07/1947', 'm' , 6) #7
player9 = Player('Donald', 'Trump', '14/06/1946', 'm' , 10) #10
player10 = Player('Brad', 'Pitt', '18/12/1963', 'm', 13) #3
#players = [player1,player2,player3,player4,player5,player6,player7,player8]

player_Rins = Player('Alex', 'Rins', '25', 'Man', 9)
player_Martin = Player('Jorge', 'Martin', '23', 'Man', 13)
player_Mir = Player('Joan', 'Mir', '23', 'Man', 4)
player_Rossi = Player('Valentino', 'Rossi', '42', 'Man', 21)
player_Miller = Player('Jack', 'Mille', '26', 'Man', 6)
player_Marquez = Player('Marc', 'Marquez', '28', 'Man', 15)
player_Zarco = Player('Johan', 'Zarco', '30', 'Man', 5)
player_Morbidelli = Player('Franco', 'Morbidelli', '26', 'Man', 8)
players = [player_Rins, player_Martin, player_Mir, player_Rossi, player_Miller, player_Marquez, player_Zarco, player_Morbidelli]




if __name__ == "__main__":

    run = TournamentControler(players)
    run.start_tournament()
    run.run_first_round('Round 1')
    for i in range (3):
        round_name = 'Round ' + str(2 + i)
        run.run_next_round(round_name)
    run.close_tournament()
