# -*-coding: utf-8 -*
#! /usr/bin/env python
"""This file is a exercice about a program for help the chess tournament organization.
It is a first program with MVC structuring."""

import sys
sys.path[:0]=['../']
from controler.tournamentControler import TournamentControler

if __name__ == "__main__":
    run = TournamentControler()
    test = run.run_first_round()
    for i in range (3):
        round_name = 'Round ' + str(2 + i)
        test = run.run_next_round(round_name)