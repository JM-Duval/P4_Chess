# -*-coding: utf-8 -*
#! /usr/bin/env python
"""This file is a exercice about a program for help the chess tournament organization.
It is a first program with MVC structuring."""

import sys
sys.path[:0]=['../']
from controler.tournamentControler import TournamentControler
from model.dataBaseTournamentModel import DataTournament


if __name__ == "__main__":

    """
    run = TournamentControler()
    test = run.start_tournament()
    run.run_first_round('Round 1')

    round_name = 'Round 2'
    test = run.run_next_round(round_name)



    for i in range (3):
        round_name = 'Round ' + str(2 + i)
        test = run.run_next_round(round_name)
    test = run.close_tournament()

    def display_match(round, match):
        matchs = DataTournamentPlayers('Word_tour_Tournament', round)
        if match == 1:
            print(matchs.load()[0].first_name, matchs.load()[0].score,
                  matchs.load()[1].first_name, matchs.load()[1].score)
        elif match == 2:
            print(matchs.load()[2].first_name, matchs.load()[2].score,
                  matchs.load()[3].first_name, matchs.load()[3].score)
        elif match == 3:
            print(matchs.load()[4].first_name, matchs.load()[4].score,
                  matchs.load()[5].first_name, matchs.load()[5].score)
        elif match == 4:
            print(matchs.load()[6].first_name, matchs.load()[6].score,
                  matchs.load()[7].first_name, matchs.load()[7].score)

    display_match('Round 1', 1)
    display_match('Round 1', 2)
    display_match('Round 1', 3)
    display_match('Round 1', 4)

    
    
    round_1 = DataTournamentPlayers(run.get_infos_tournament().name_tournament,
                                        run.get_infos_tournament().rounds[0].round_name)
    matchs_in_round_1 = run.get_infos_tournament().rounds[0].matchs

    for player in matchs_in_round_1:
        round_1.insert_player(player.player1)
        round_1.insert_player(player.player2)

    """

# -- Reprendre un tournoi en cours -----------------

    #run = TournamentControler()
test = DataTournament('Word_tour_Tournament_5')

for i in test.load():
    print (i.status)
    print (type(i))
    #for x in i:
    #    print (x)
