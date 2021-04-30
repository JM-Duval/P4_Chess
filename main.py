# -*-coding: utf-8 -*
#! /usr/bin/env python
"""This file is a exercice about a program for help the chess tournament organization.
It is a first program with MVC structuring."""

import sys
sys.path[:0]=['../']
from controler.tournamentControler import TournamentControler



if __name__ == "__main__":
    run = TournamentControler()
    test = run.start_tournament()
    run.run_first_round('Round 1')
    for i in range (3):
        round_name = 'Round ' + str(2 + i)
        test = run.run_next_round(round_name)
    test = run.close_tournament()


    """
    test = run.run_first_round('Round 1')
    for i in range (3):
        round_name = 'Round ' + str(2 + i)
        test = run.run_next_round(round_name)
    test = run.close_tournament()
    """


    # -- Round 1 ---------------------------

    """
    
    # -- Other Rounds ----------------------
    for i in range(3):
        #round_name = 'Round ' + str(i+2)
        #run.run_next_round(round_name)
        run.run_next_round()
        roundx = DataTournamentPlayers(run.get_infos_tournament().name_tournament,
                                       run.get_infos_tournament().rounds[i+1].round_name)
        matchs_in_roundx = run.get_infos_tournament().rounds[i+1].matchs
        for player in matchs_in_roundx:
            roundx.insert_player(player.player1)
            roundx.insert_player(player.player2)
        #print(run.get_infos_tournament().rounds[i+1].round_name)

    run.close_tournament()

    #"""

    # -- Chargement des données du tournoi ---------------------------------
    """
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

    def display_list_tournament():
        import glob
        return glob.glob('*.json')

    for i in display_list_tournament():
        print (i)

    print (len(display_list_tournament()))
    round_1 = DataTournamentPlayers(run.get_infos_tournament().name_tournament,
                                        run.get_infos_tournament().rounds[0].round_name)
    matchs_in_round_1 = run.get_infos_tournament().rounds[0].matchs

    for player in matchs_in_round_1:
        round_1.insert_player(player.player1)
        round_1.insert_player(player.player2)




    """

# -- Reprendre un tournoi en cours -----------------

