# -*-coding: utf-8 -*
# !/usr/bin/env python
"""This file is a exercice about a program for help the chess tournament organization.
It is a first program with MVC structuring."""

from controler.menuControler import main_menu
import sys
sys.path[:0] = ['../']


if __name__ == "__main__":
    main_menu()
