# P4_Chess

## Pr�sentation

Ce programme est une version beta d'un script permettant de g�rer des tournois d'�checs hors ligne. 

Les objectifs de ce programme sont les suivants:

- g�n�rer des tournois (gestion des joueurs / matchs / rounds / classement)

- automatiser le classement des joueurs apr�s chaque fin de tournoi

- g�rer la base de donn�es des joueurs

- proposer des rapports de statistiques des joueurs et des tournois

## Pour commencer

Les instructions ci dessous vous aiderons � ex�cuter correctement ce programme.

## Pr�-requis

* Python 3 install� [T�l�charger Python](https://www.python.org/downloads/)
* Savoir naviguer dans les dossiers & fichiers � partir d'un terminal.

## Installation

Pour un bon fonctionnement, il est pr�f�rable d'ex�cuter le programme dans un environnement virtuel. Pour cela, ci dessous les �tapes � suivre:

1. **T�l�chargement du projet.**

    1. Depuis votre terminal, placez vous � l'endroit souhait�:
    
    ```cd [chemin d'acc�s]```  
    
    2. Creer un nouveau dossier:
    
    ```mkdir [nom de votre dossier]```
    
    3. Copier le programme source:
    
    ```git clone https://github.com/JM-Duval/P4_Chess.git```
    

Vous devez voir (depuis votre explorateur) les fichiers suivants: * main.py * requirements.txt, ainsi que les dossiers suivant: controler / model / view.

Dans le dossier *controler* doit apparaitre les fichiers: 

 * dataBasePlayersControler.py 
 * inputUserControler.py
 * menuControler.py
 * tournamentControler.py

Dans le dossier *model* doit apparaitre les fichiers: 

 * dataBasePlayersModel.py 
 * dataBaseTournamentModel.py 
 * inputUserModel.py 
 * match.py 
 * menuModel.py 
 * player.py 
 * round.py 
 * tournament.py

Dans le dossier *view* doit apparaitre les fichiers:
 
 * dataBasePlayersView.py 
 * menuView.py 
 * tournamentView.py 
 * inputUserView.py

2. **Creer un environnement virtuel.**

Depuis windows/mac/linux: ```python3 -m venv env```

3. **Activer l'environnement.**

Depuis windows: ```env\Scripts\activate.bat```

Depuis mac/linux: ```source env/bin/activate```

Si vous rencontrez des difficult�s ou si vous souhaitez plus de d�tails sur l'installation d'un environnement virtuel, vous pouvez vous reporter � la documentation Python:
[Documentation Python](https://www.python.org/doc/)

4. **Installer les paquets.**

```pip install -r requirements.txt```

En executant la commande: pip freeze, vous devez voir apparaitre cette liste: 
- flake8==3.9.2
- flake8-html==0.4.1
- importlib-metadata==4.5.0
- Jinja2==3.0.1
- keyboard==0.13.5
- MarkupSafe==2.0.1
- mccabe==0.6.1
- pycodestyle==2.7.0
- pyflakes==2.3.1
- Pygments==2.9.0
- tinydb==4.4.0
- zipp==3.4.1


5. **Lancement du programme.**

```pyhton main.py```

Losque vous allez lancer le programme depuis le terminal, vous allez voir apparaitre le menu principale. Il vous suffit ensuite de suivre les indications pour naviguer des les menus et sous menus. 

## Fabriqu� avec
[PyCharm Community Edition 2020.2.3 x64](https://pycharm-community-edition.fr.softonic.com/) - Editeur de textes


## Auteurs

* **JM Duval** 

