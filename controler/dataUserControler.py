# -*-coding: utf-8 -*
#! /usr/bin/env python
"""This file is a exercice about a program for help the chess tournament organization.
It is a first program with MVC structuring."""

import datetime


class CheckData:

    def __init__(self, data_input):
        self.data_input = data_input
        self.letters = "abcdefghijklmnopqrstuvwxyz_"
        self.numbers = "1234567890"
        self.year_birt_min = int(datetime.datetime.today().strftime('%Y')) - 120
        self.year_birt_max = int(datetime.datetime.today().strftime('%Y')) - 10
        self.list_sexe = {'man', 'women'}
        self.time_controler = {'1', '2', '3'} # bullet // blitz // coup rapide

    def word(self):
        if len(self.data_input) <2:
            return False
        for i in self.data_input:
            if i in self.letters:
               continue
            else:
                print("Conditions d'un mot correct : \n - Minimum 2 lettres \n"
                      " - Caractères autorisés: abcdefghijklmnopqrstuvwxyz_ \n"
                      " - Tout en minuscule")
                return False

    def number (self):
        for i in self.data_input:
            if i in self.numbers:
                continue
            else:
                print(" -- Data input incorrect -- \n"
                      "Conditions d'un nombre correct : \n - Pas d'espace \n"
                      " - Caractères autorisés: 1234567890")
                return False

    def date (self):
        for i in self.data_input:
            if i in self.numbers:
                continue
            else:
                return False
        if int(self.data_input) in range(self.year_birt_min, self.year_birt_max):
            return True
        else:
            print(f'Saisir une année entre {self.year_birt_min} & {self.year_birt_max}')
            return False

    def sexe (self):
        if self.data_input in self.list_sexe:
            return True
        else:
            print ("Saisir : man or women")
            return False

    def time_control(self):
        if self.data_input in self.time_controler:
            return True
        else:
            return False


def enter_word(word):
    word_input = input(f"{word} : ")
    check = CheckData(word_input)
    while check.word() == False:
        word_input = input(f"{word} : ")
        check = CheckData(word_input)
    return word_input

def enter_number(number):
    nb = input(f"{number} : ")
    check = CheckData(nb)
    while check.number() == False:
        nb = input(f"{number} : ")
        check = CheckData(nb)
    return nb

def enter_year_of_birth():
    year_of_birth = input('year of birth :')
    check_year_of_birth = CheckData(year_of_birth)
    while check_year_of_birth.date() == False:
        year_of_birth = input('year of birth :')
        check_year_of_birth = CheckData(year_of_birth)
    return year_of_birth

def enter_sexe():
    sexe = input("Man or Women :").lower()
    check_sexe = CheckData(sexe)
    while check_sexe.sexe() == False:
        sexe = input("Man or Women :")
        check_sexe = CheckData(sexe)
    return sexe

def enter_time_controler():
    controleur = input("Time Controler : \n"
                      " Bullet  // Tapez 1 \n"
                      " Blitz  // Tapez 2 \n"
                      " Coup rapide // Tapez 3 \n")
    check_controleur = CheckData(controleur)
    while check_controleur.time_control() == False:
        controleur = input("Time Controler : \n"
                          " Bullet  // Tapez 1 \n"
                          " Blitz  // Tapez 2 \n"
                          " Coup rapide // Tapez 3 \n")
        check_controleur = CheckData(controleur)
    return controleur


#first_name = enter_word('first name player')
#last_name = enter_word('last name player')
#elo = enter_number('elo')
#year_of_birth = enter_year_of_birth()
#sexe = enter_sexe()
#print (f'PLayer saved : | {first_name} {last_name} : elo:{elo} : {year_of_birth} : sexe : {sexe} |')

controleur = enter_time_controler()
print (f'{controleur}')











"""
data input:
    > players  (first_name, last_name, date_birth, sexe, elo)
    > infos tournament  (name_tournament, location, start_time, tour_number, time_control)
    > players for tournament
    > matchs results

def creerGenerateur(mot):
    letters = "abcdefghijklmnopqrstuvwxyz_"
    for i in mot:
        if i in letters:
            continue
        else:
            yield i

name = input ('your name? : ')
generateur = creerGenerateur(name)
for i in generateur:
    reply = []
    if i != '':
        reply.append(i)
    




    if mot.isalpha() == True:
        print ("Mot correct")
    else:
        print ("Veuillez ecrire un mot uniquement en lettre")

    def help_correct_word(self):
        print("Conditions d'un mot correct : \n - Minimum 2 lettres \n"
              " - Caractères autorisés: abcdefghijklmnopqrstuvwxyz_ \n"
              " - Tout en minuscule")

    def help_correct_number(self):
        print(" -- Data input incorrect -- \n"
              "Conditions d'un nombre correct : \n - Pas d'espace \n"
              " - Caractères autorisés: 1234567890")

    def help_correct_date_of_birth(self):
        year_birt_min = int(datetime.datetime.today().strftime('%Y')) - 120
        year_birt_max = int(datetime.datetime.today().strftime('%Y')) - 10
        print(f'Saisir une année entre {year_birt_min} & {year_birt_max}')




"""
