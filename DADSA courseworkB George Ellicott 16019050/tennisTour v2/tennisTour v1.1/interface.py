##Author: George Ellicott 16019050
##created 22/03/2018
##revised: 22/03/2018 - added comments
##An simulation of a tennis year, recording ranking poimts and prize money
##User advice: none
import cProfile
# import re
# cProfile.run('re.compile("interface")')
import csv
import Player_Ranking_PrizeMoney
import Player_Data_Tac1
import Player_Data_TAE21
import Player_Data_Taw11
import Player_Data_Tbs2
import Player_Data_All
import tac1_ranking
import tae21_ranking
import taw11_ranking
import tbs2_ranking
import operator
import math
import itertools
import sys
# global arrays used throughout program
maleLeaderBoard = []
femaleLeaderBoard = []
malePlayerNamesDatatableTac1 = []
malePlayerNamesDatatableTae21 = []
malePlayerNamesDatatableTaw11 = []
malePlayerNamesDatatableTbs2 = []
malePlayerNamesDatatableAll = []
femalePlayerNamesDatatableTac1 = []
femalePlayerNamesDatatableTae21 = []
femalePlayerNamesDatatableTaw11 = []
femalePlayerNamesDatatableTbs2 = []
femalePlayerNamesDatatableAll = []
tac1_ranking_points_list_mens = []
tae21_ranking_points_list_mens = []
taw11_ranking_points_list_mens = []
tbs2_ranking_points_list_mens = []
tac1_ranking_points_list_womens = []
tae21_ranking_points_list_womens = []
taw11_ranking_points_list_womens = []
tbs2_ranking_points_list_womens = []

def exitProgam():
    print("exitProgam\n")

#Description: Prints list of players names, then loads menu function
#parameters: none
#return type: none
def listPlayers():
    """Display list of players."""
    print("listPlayers\n")
    print("Male Players\n")
    print("---------------------------------------------------------------------------")
    for player in maleLeaderBoard:
        print(player._name)
    print("---------------------------------------------------------------------------")
    print("Female Players\n")
    print("---------------------------------------------------------------------------")
    for player in femaleLeaderBoard:
        print(player._name)
    print("---------------------------------------------------------------------------")
    menu()

#Description: Calculates the number rounds within a given tournament, from the number of players within the selected gender, can be scaled up/down
#parameters: mensOrWomens - String
#return type: numberOfRounds - integer
def sizeOfTournament(mensOrWomens):
    """Calculates the number rounds within the tournament."""
    numberOfplayers = 0
    numberOfRounds = 0
    if mensOrWomens == 'MEN':
        for players in maleLeaderBoard:
              numberOfplayers = numberOfplayers + 1
    elif mensOrWomens == 'LADIES':
        for players in femaleLeaderBoard:
            numberOfplayers = numberOfplayers + 1
    while numberOfplayers != 1:
        numberOfplayers = numberOfplayers / 2
        numberOfRounds = numberOfRounds + 1
    return numberOfRounds

#Description: Creates the object player, from class - Player_Ranking_PrizeMoney
#parameters: none
#return type: none
def malePlayers():#initialize male players
    """Creates the objects player"""
    with open('MALE PLAYERS.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        malePlayerNames = []
        for row in reader:
            malePlayerNames.append(row['MALE PLAYERS'])
            player = Player_Ranking_PrizeMoney.Player_Ranking_PrizeMoney(row['MALE PLAYERS'],0,0,0) #parameters - player name, ranking, prizeMoney
            maleLeaderBoard.append(player)

def dataMalePlayersAll():#initialize male data of players
    """Creates the objects player data"""
    with open('MALE PLAYERS.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            playerdataAll = Player_Data_All.Player_Data_All(row['MALE PLAYERS'],0,0,0,0,0) #parameters - player name, ranking, prizeMoney
            malePlayerNamesDatatableAll.append(playerdataAll)

def dataMalePlayersTac1():#initialize male data of players
    """Creates the objects player data"""
    with open('MALE PLAYERS.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            playerdataTac1 = Player_Data_Tac1.Player_Data_Tac1(row['MALE PLAYERS'],0,0,0,0,0) #parameters - player name, ranking, prizeMoney
            malePlayerNamesDatatableTac1.append(playerdataTac1)


def tac1_ranking_intz():#initialize male data of players
    """Creates the objects player data"""
    with open('MALE PLAYERS.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            player_ranking_tac1 = tac1_ranking.tac1_ranking(row['MALE PLAYERS'],0,0) #parameters - player name, ranking, prizeMoney
            tac1_ranking_points_list_mens.append(player_ranking_tac1)

def tae21_ranking_intz():#initialize male data of players
    """Creates the objects player data"""
    with open('MALE PLAYERS.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            player_ranking_tae21 = tae21_ranking.tae21_ranking(row['MALE PLAYERS'],0,0) #parameters - player name, ranking, prizeMoney
            tae21_ranking_points_list_mens.append(player_ranking_tae21)

def taw11_ranking_intz():#initialize male data of players
    """Creates the objects player data"""
    with open('MALE PLAYERS.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            player_ranking_taw11 = taw11_ranking.taw11_ranking(row['MALE PLAYERS'],0,0) #parameters - player name, ranking, prizeMoney
            taw11_ranking_points_list_mens.append(player_ranking_taw11)

def tbs2_ranking_intz():#initialize male data of players
    """Creates the objects player data"""
    with open('MALE PLAYERS.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            player_ranking_tbs2 = tbs2_ranking.tbs2_ranking(row['MALE PLAYERS'],0,0) #parameters - player name, ranking, prizeMoney
            tbs2_ranking_points_list_mens.append(player_ranking_tbs2)

def tac1_ranking_intzW():#initialize male data of players
    """Creates the objects player data"""
    with open('FEMALE PLAYERS.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            player_ranking_tac1 = tac1_ranking.tac1_ranking(row['FEMALE PLAYERS'],0,0) #parameters - player name, ranking, prizeMoney
            tac1_ranking_points_list_womens.append(player_ranking_tac1)

def tae21_ranking_intzW():#initialize male data of players
    """Creates the objects player data"""
    with open('FEMALE PLAYERS.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            player_ranking_tae21 = tae21_ranking.tae21_ranking(row['FEMALE PLAYERS'],0,0) #parameters - player name, ranking, prizeMoney
            tae21_ranking_points_list_womens.append(player_ranking_tae21)

def taw11_ranking_intzW():#initialize male data of players
    """Creates the objects player data"""
    with open('FEMALE PLAYERS.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            player_ranking_taw11 = taw11_ranking.taw11_ranking(row['FEMALE PLAYERS'],0,0) #parameters - player name, ranking, prizeMoney
            taw11_ranking_points_list_womens.append(player_ranking_taw11)

def tbs2_ranking_intzW():#initialize male data of players
    """Creates the objects player data"""
    with open('FEMALE PLAYERS.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            player_ranking_tbs2 = tbs2_ranking.tbs2_ranking(row['FEMALE PLAYERS'],0,0) #parameters - player name, ranking, prizeMoney
            tbs2_ranking_points_list_womens.append(player_ranking_tbs2)

def dataMalePlayersTae21():#initialize male data of players
    """Creates the objects player data"""
    with open('MALE PLAYERS.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            playerdataTAE21 = Player_Data_TAE21.Player_Data_TAE21(row['MALE PLAYERS'],0,0,0,0,0) #parameters - player name, ranking, prizeMoney
            malePlayerNamesDatatableTae21.append(playerdataTAE21)

def dataMalePlayersTaw11():#initialize male data of players
    """Creates the objects player data"""
    with open('MALE PLAYERS.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            playerdataTaw11 = Player_Data_Taw11.Player_Data_Taw11(row['MALE PLAYERS'],0,0,0,0,0) #parameters - player name, ranking, prizeMoney
            malePlayerNamesDatatableTaw11.append(playerdataTaw11)

def dataMalePlayersTbs2():#initialize male data of players
    """Creates the objects player data"""
    with open('MALE PLAYERS.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            playerdataTbs2 = Player_Data_Tbs2.Player_Data_Tbs2(row['MALE PLAYERS'],0,0,0,0,0) #parameters - player name, ranking, prizeMoney
            malePlayerNamesDatatableTbs2.append(playerdataTbs2)

def dataFemalePlayersAll():#initialize male data of players
    """Creates the objects player data"""
    with open('FEMALE PLAYERS.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            playerdataLadiesAll = Player_Data_All.Player_Data_All(row['FEMALE PLAYERS'],0,0,0,0,0) #parameters - player name, ranking, prizeMoney
            femalePlayerNamesDatatableAll.append(playerdataLadiesAll)

def dataFemalePlayersTac1():#initialize female data of players
    """Creates the objects player data"""
    with open('FEMALE PLAYERS.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            playerdataTac1 = Player_Data_Tac1.Player_Data_Tac1(row['FEMALE PLAYERS'],0,0,0,0,0) #parameters - player name, ranking, prizeMoney
            femalePlayerNamesDatatableTac1.append(playerdataTac1)

def dataFemalePlayersTae21():#initialize female data of players
    """Creates the objects player data"""
    with open('FEMALE PLAYERS.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            playerdataTAE21 = Player_Data_TAE21.Player_Data_TAE21(row['FEMALE PLAYERS'],0,0,0,0,0) #parameters - player name, ranking, prizeMoney
            femalePlayerNamesDatatableTae21.append(playerdataTAE21)

def dataFemalePlayersTaw11():#initialize female data of players
    """Creates the objects player data"""
    with open('FEMALE PLAYERS.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            playerdataTaw11 = Player_Data_Taw11.Player_Data_Taw11(row['FEMALE PLAYERS'],0,0,0,0,0) #parameters - player name, ranking, prizeMoney
            femalePlayerNamesDatatableTaw11.append(playerdataTaw11)

def dataFemalePlayersTbs2():#initialize female data of players
    """Creates the objects player data"""
    with open('FEMALE PLAYERS.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            playerdataTbs2 = Player_Data_Tbs2.Player_Data_Tbs2(row['FEMALE PLAYERS'],0,0,0,0,0) #parameters - player name, ranking, prizeMoney
            femalePlayerNamesDatatableTbs2.append(playerdataTbs2)


def printdata():
    #initialize mens data
    dataMalePlayersTac1()
    dataMalePlayersTae21()
    dataMalePlayersTaw11()
    dataMalePlayersTbs2()
    dataMalePlayersAll()
    #initialize ladies data
    dataFemalePlayersTac1()
    dataFemalePlayersTae21()
    dataFemalePlayersTaw11()
    dataFemalePlayersTbs2()
    dataFemalePlayersAll()
     #initialize tournament individual data
    tac1_ranking_intz()
    tae21_ranking_intz()
    taw11_ranking_intz()
    tbs2_ranking_intz()
    #initialize tournament individual data
    tac1_ranking_intzW()
    tae21_ranking_intzW()
    taw11_ranking_intzW()
    tbs2_ranking_intzW()

#Description: Creates the object player, from class - Player_Ranking_PrizeMoney
#parameters: none
#return type: none
def femalePlayers(): #initialize female players
    """Creates the objects player"""
    with open('FEMALE PLAYERS.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        malePlayerNames = []
        for row in reader:
            malePlayerNames.append(row['FEMALE PLAYERS'])
            player = Player_Ranking_PrizeMoney.Player_Ranking_PrizeMoney(row['FEMALE PLAYERS'],0,0,0) #parameters - player name, ranking, prizeMoney
            femaleLeaderBoard.append(player)

#Description: Takes the choices, displays desired output of rankings
#parameters: none
#return type: none
def viewRankings():
     """Takes the choices, displays desired output."""
     sexmenuRankingsInput = input('Enter M for Male tables or F for Female tables: ')
     sexmenuRankingsInput = sexmenuRankingsInput.strip()
     sexmenuRankingsInput = sexmenuRankingsInput.upper()
     if sexmenuRankingsInput == 'M':
        print("1.Mens Rankings\n")
        print("2.Mens prizemoney\n")
        print("3.Menu\n")
        rankingOrPrizemoneyView = input('Enter a number 1, 2 or 3: ')
        rankingOrPrizemoneyView = rankingOrPrizemoneyView.strip()
        if rankingOrPrizemoneyView == '1':
            mensRankings()
        if rankingOrPrizemoneyView == '2':
            mensPrizeMoneyRankings()
        if rankingOrPrizemoneyView == '3':
            menu()
     if sexmenuRankingsInput == 'F':
        print("1.Ladies Rankings\n")
        print("2.Ladies prizemoney\n")
        print("3.Menu\n")
        rankingOrPrizemoneyView = input('Enter a number 1, 2 or 3: ')
        rankingOrPrizemoneyView = rankingOrPrizemoneyView.strip()
        if rankingOrPrizemoneyView == '1':
            womensRankings()
        if rankingOrPrizemoneyView == '2':
            womensPrizeMoneyRankings()
        if rankingOrPrizemoneyView == '3':
            menu()

#Description: Sorts by attribute player rankings then prints list of objects attributes player name and player ranking
#parameters: none
#return type: none
def mensRankings():
    """Prints and sorts the rankings"""
    print("1.TAC1 \n")
    print("2.TAE21 \n")
    print("3.TAW11 \n")
    print("4.TBS2 \n")
    print("5.ALL TOURNAMENTS")
    rankingInput = input("Selected a numbeer 1-5")
    if rankingInput == '1':
         print("TAC1 Prize Money")
         tac1_ranking_points_list_mens.sort(key = lambda player: player._ranking, reverse=True)
         for player_ranking_tac1 in tac1_ranking_points_list_mens:
             print(player_ranking_tac1._name , str(player_ranking_tac1._ranking) )
    elif rankingInput == '2':
        print("TAE21 Prize Money")
        tae21_ranking_points_list_mens.sort(key = lambda player: player._ranking, reverse=True)
        for player_ranking_tae21 in tae21_ranking_points_list_mens:
             print(player_ranking_tae21._name , str(player_ranking_tae21._ranking) )
    elif rankingInput == '3':
        print("TAW11 Prize Money")
        taw11_ranking_points_list_mens.sort(key = lambda player: player._ranking, reverse=True)
        for player_ranking_taw11 in taw11_ranking_points_list_mens:
             print(player_ranking_taw11._name , str(player_ranking_taw11._ranking) )
    elif rankingInput == '4':
        print("TBS2 Prize Money")
        tbs2_ranking_points_list_mens.sort(key = lambda player: player._ranking, reverse=True)
        for player_ranking_tbs2 in tbs2_ranking_points_list_mens:
             print(player_ranking_tbs2._name , str(player_ranking_tbs2._ranking) )
    elif rankingInput == '5':
        print("mens Ranking table")
        positon = 1
        maleLeaderBoard.sort(key = lambda player: player._ranking, reverse=True)
        for player in maleLeaderBoard:
            print(positon,player._name, player._ranking)
            positon = positon + 1
    menu()



#Description: Sorts by attribute player prize money then prints list of objects attributes player name and player prizeMoney
#parameters: none
#return type: none
def mensPrizeMoneyRankings():
    """Prints and sorts the prize money"""
    print("1.TAC1 \n")
    print("2.TAE21 \n")
    print("3.TAW11 \n")
    print("4.TBS2 \n")
    print("5.ALL TOURNAMENTS")
    rankingInput = input("Selected a numbeer 1-5")
    if rankingInput == '1':
         print("TAC1 Prize Money")
         tac1_ranking_points_list_mens.sort(key = lambda player: player._prizeMoney, reverse=True)
         for player_ranking_tac1 in tac1_ranking_points_list_mens:
             print(player_ranking_tac1._name , str(player_ranking_tac1._prizeMoney) )
    elif rankingInput == '2':
        print("TAE21 Prize Money")
        tae21_ranking_points_list_mens.sort(key = lambda player: player._prizeMoney, reverse=True)
        for player_ranking_tae21 in tae21_ranking_points_list_mens:
             print(player_ranking_tae21._name , str(player_ranking_tae21._prizeMoney) )
    elif rankingInput == '3':
        print("TAW11 Prize Money")
        taw11_ranking_points_list_mens.sort(key = lambda player: player._prizeMoney, reverse=True)
        for player_ranking_taw11 in taw11_ranking_points_list_mens:
             print(player_ranking_taw11._name , str(player_ranking_taw11._prizeMoney) )
    elif rankingInput == '4':
        print("TBS2 Prize Money")
        tbs2_ranking_points_list_mens.sort(key = lambda player: player._prizeMoney, reverse=True)
        for player_ranking_tbs2 in tbs2_ranking_points_list_mens:
             print(player_ranking_tbs2._name , str(player_ranking_tbs2._prizeMoney) )
    elif rankingInput == '5':
        positon = 1
        print("mens Prize Money Rankings table")
        maleLeaderBoard.sort(key = lambda player: player._prizeMoney, reverse=True)
        for player in maleLeaderBoard:
            print(positon ,player._name, player._prizeMoney)
            positon = positon + 1
    menu()
#Description: Sorts by attribute player prize money then prints list of objects attributes player name and player prizeMoney
#parameters: none
#return type: none
def womensPrizeMoneyRankings():
    """Prints and sorts the prize money"""
    print("1.TAC1 \n")
    print("2.TAE21 \n")
    print("3.TAW11 \n")
    print("4.TBS2 \n")
    print("5.ALL TOURNAMENTS")
    rankingInput = input("Selected a numbeer 1-5")
    if rankingInput == '1':
         print("TAC1 Prize Money")
         tac1_ranking_points_list_womens.sort(key = lambda player: player._prizeMoney, reverse=True)
         for player_ranking_tac1 in tac1_ranking_points_list_womens:
             print(player_ranking_tac1._name , str(player_ranking_tac1._prizeMoney) )
    elif rankingInput == '2':
        print("TAE21 Prize Money")
        tae21_ranking_points_list_womens.sort(key = lambda player: player._prizeMoney, reverse=True)
        for player_ranking_tae21 in tae21_ranking_points_list_womens:
             print(player_ranking_tae21._name , str(player_ranking_tae21._prizeMoney) )
    elif rankingInput == '3':
        print("TAW11 Prize Money")
        taw11_ranking_points_list_womens.sort(key = lambda player: player._prizeMoney, reverse=True)
        for player_ranking_taw11 in tae21_ranking_points_list_womens:
             print(player_ranking_taw11._name , str(player_ranking_taw11._prizeMoney) )
    elif rankingInput == '4':
        print("TBS2 Prize Money")
        tbs2_ranking_points_list_womens.sort(key = lambda player: player._prizeMoney, reverse=True)
        for player_ranking_tbs2 in tbs2_ranking_points_list_womens:
             print(player_ranking_tbs2._name , str(player_ranking_tbs2._prizeMoney) )
    elif rankingInput == '5':
        positon = 1
        print("Ladies Prize Money Rankings table")
        femaleLeaderBoard.sort(key = lambda player: player._prizeMoney, reverse=True)
        for player in femaleLeaderBoard:
             print(positon ,player._name, player._prizeMoney)
             positon = positon + 1
    menu()
#Description: Sorts by attribute player rankings then prints list of objects attributes player name and player ranking
#parameters: none
#return type: none
def womensRankings():
    """Prints and sorts the rankings"""
    print("1.TAC1 \n")
    print("2.TAE21 \n")
    print("3.TAW11 \n")
    print("4.TBS2 \n")
    print("5.ALL TOURNAMENTS")
    rankingInput = input("Selected a numbeer 1-5")
    if rankingInput == '1':
         print("TAC1 Prize Money")
         tac1_ranking_points_list_womens.sort(key = lambda player: player._ranking, reverse=True)
         for player_ranking_tac1 in tac1_ranking_points_list_womens:
             print(player_ranking_tac1._name , str(player_ranking_tac1._ranking) )
    elif rankingInput == '2':
        print("TAE21 Prize Money")
        tae21_ranking_points_list_womens.sort(key = lambda player: player._ranking, reverse=True)
        for player_ranking_tae21 in tae21_ranking_points_list_mens:
             print(player_ranking_tae21._name , str(player_ranking_tae21._ranking) )
    elif rankingInput == '3':
        print("TAW11 Prize Money")
        taw11_ranking_points_list_womens.sort(key = lambda player: player._ranking, reverse=True)
        for player_ranking_taw11 in taw11_ranking_points_list_womens:
             print(player_ranking_taw11._name , str(player_ranking_taw11._ranking) )
    elif rankingInput == '4':
        print("TBS2 Prize Money")
        tbs2_ranking_points_list_womens.sort(key = lambda player: player._ranking, reverse=True)
        for player_ranking_tbs2 in tbs2_ranking_points_list_womens:
             print(player_ranking_tbs2._name , str(player_ranking_tbs2._ranking) )
    elif rankingInput == '5':
        print("Ladies Ranking table")
        femaleLeaderBoard.sort(key = lambda player: player._ranking, reverse=True)
    for player in femaleLeaderBoard:
        positon = 1
        print(positon ,player._name, player._ranking)
        positon = positon + 1
    menu()

#Description: Calculates the round points by checking where the player finished (1st arg)and which tournament (2nd arg)
#then matching that to the place column in the RANKING POINTS.csv
#parameters: finished - String, tournament - String
#return type: totalPoints - float 2dp
def rankings(finished, tournament):
    place = finished
    placePoints = 0.0
    with open('RANKING POINTS.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if place == row['Place']:
                placePoints = row['Tournament Ranking  Points']
                placePoints = float(placePoints)
    placePoints = round(placePoints, 2)
    return placePoints
# takes in round points then * by max bonus
def bonusPointsMaxMethod(roundpoints):
    bonus = (roundpoints*2.5)
    bonus = round(bonus,2)
    return bonus
# takes in round points then * by min bonus
def bonusPointsMinMethod(roundpoints):
    bonus = (roundpoints*1.5)
    bonus = round(bonus,2)
    return bonus
# takes in round points then * by difficulty
def totalRoundPoints(tournament,roundpoints):
    if tournament == 'TAC1':
        totalpoints = (roundpoints*2.7)
        return totalpoints
    elif tournament == 'TAE21':
        totalpoints = (roundpoints*2.3)
        return totalpoints
    elif tournament == 'TAW11':
        totalpoints = (roundpoints*3.1)
        return totalpoints
    elif tournament == 'TBS2':
        totalpoints = (roundpoints*3.25)
        return totalpoints
    else:
        print("that tournament does not exist")
#Description: Calculates the round points by checking where the player finished/position (1st arg)
#and which tournament (2nd arg) then matching that to the place column in the PRIZE MONEY.csv
#parameters: finished - String, tournament - String
#return type: totalPoints - integer
def prizeMoneyFromTournament(finished, tournament):
    place = finished
    prizemoney = 0
    with open('PRIZE MONEY.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if place == row['Place'] and tournament == row['Tournament']:
                prizemoney = row['Prize Money ($)']
                prizemoney = int(prizemoney)
    return prizemoney
#Description: Gives user selection on male/female tournament, selection of tournament
#then passes selections into function to load correct manual input tournament selections.
#parameters: none
#return type: none
def tournamentsViaManualInput():
    with open('TOURNAMENT NAME.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        tournamentNames = []
        for row in reader:
            tournamentNames.append(row['Tournament'])
    genderMenuInput = input('Enter M for Male tournaments or F for Female tournaments: ')
    genderMenuInput = genderMenuInput.strip()
    genderMenuInput = genderMenuInput.upper()
    if genderMenuInput == 'M':
        mensOrWomens = 'MEN'
    elif genderMenuInput == 'F':
        mensOrWomens = 'LADIES'
    else:
        print("not a valid input")
        tournamentsViaManualInput()
    print('Tournaments')
    print('1.'+tournamentNames[0]+'\n')
    print('2.'+tournamentNames[1]+'\n')
    print('3.'+tournamentNames[2]+'\n')
    print('4.'+tournamentNames[3]+'\n')
    tournamentMenuInput = input('Enter a number 1-4: ')
    tournamentMenuInput = tournamentMenuInput.strip()
    if tournamentMenuInput == '1':
        tournament = tournamentNames[0]
        tennisRound(tournament,mensOrWomens,1)
    elif tournamentMenuInput == '2':
        tournament = tournamentNames[1]
        tennisRound(tournament,mensOrWomens,1)
    elif tournamentMenuInput == '3':
        tournament = tournamentNames[2]
        tennisRound(tournament,mensOrWomens,1)
    elif tournamentMenuInput == '4':
        tournament = tournamentNames[3]
        tennisRound(tournament,mensOrWomens,1)
    else:
        print('Invalid input, try again')
        tournamentsViaManualInput()
#Description: processes the selected tournament (1st arg) and gender (2nd arg) by manual input
#taken from the console and gives corresponding ranking points and prize money to player object
#parameters: tournament - String, mensOrWomens - String
#return type: none
def tennisRound(tournament,mensOrWomens,TourRound):
    winner = []
    TournamentRound = TourRound
    sizeOfroundsForLoop = sizeOfTournament(mensOrWomens)
    numberOfplayers = 0
    prizeMoney = 0
    totalpoints =0
    basepoints = 0
    TournamentRound = int(TournamentRound)
    for x in range((TournamentRound-1), sizeOfroundsForLoop):
        exitORnot = input("Exit y/n ?")
        if exitORnot == 'y':
            maleSavedprogress()
            femaleSavedprogress()
            sys.exit()
        with open('ROUND PROGRESS.csv', 'w', newline='') as csvfile:
            fieldnames = ['ROUND', 'TOURNAMENT','GENDER']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow({'ROUND': str(TournamentRound), 'TOURNAMENT': str(tournament),'GENDER': str(mensOrWomens)})
            TournamentRound = str(TournamentRound)
            print("---------------------------------------------------------------------------")
            print(tournament + " ROUND " + str(TournamentRound) )
            print("---------------------------------------------------------------------------")
            roundpoints = 0
            totalpoints = 0
            prizeMoney = 0
            finished = 0
            TournamentRound = str(TournamentRound)
            with open('DADSA 17-18 COURSEWORK B '+tournament+' ROUND '+TournamentRound+' '+mensOrWomens+'.csv', newline='') as csvfile:
                TournamentRound = int(TournamentRound)
                TournamentRound = TournamentRound + 1
                reader = csv.DictReader(csvfile)
                doesNotAdvancedToNextRound = []
                bonusWinMaxPoints = []
                winByOne = []
                bonusPointsMin = []
                AdvancedToNextRound = []
                Choice = input("would like manual input? Y/N:")
                for row in reader:
                    if (Choice == "y"):
                        print(row['Player A'], row['Score Player A'], row['Player B'], row['Score Player B'])
                        player_score_a = input(row['Player A'])
                        player_score_b = input(row['Player B'])
                    else:
                        print(row['Player A'], row['Score Player A'], row['Player B'], row['Score Player B'])
                        player_score_a = row['Score Player A']
                        player_score_b = row['Score Player B']
                    if mensOrWomens == 'MEN':
                        while True:
                            if (not player_score_a.isdigit() or not player_score_b.isdigit()):
                                print("incorrect input - please only enter integers")
                                print("\n")
                                print(row['Player A']+ " Vs " +row['Player B'])
                                player_score_a = input(row['Player A'])
                                player_score_b = input(row['Player B'])
                            elif (int(player_score_a) >= 4) or (int(player_score_b)>= 4):
                                print("incorrect input - mens tournament must be best out of 5")
                                print("\n")
                                print(row['Player A']+ " Vs " +row['Player B'])
                                player_score_a = input(row['Player A'])
                                player_score_b = input(row['Player B'])
                            elif int(player_score_a) == int(player_score_b):
                                print("incorrect input - mens tournament no draws")
                                print("\n")
                                print(row['Player A']+ " Vs " +row['Player B'])
                                player_score_a = input(row['Player A'])
                                player_score_b = input(row['Player B'])
                            elif int(player_score_a) <= 2 and int(player_score_b)  <= 2:
                                injury = input("This is a incomplete match, was there an injury? Y/N ")
                                print(player_score_a)
                                print(player_score_b)
                                if injury == 'y':
                                    while True :
                                        print("please select a player to go through \n")
                                        print(" press A for player: " + row['Player A']+"\n")
                                        print(" press B for player: " + row['Player B']+"\n")
                                        resolved_injury = input("selection: ")
                                        if resolved_injury == 'a':
                                            player_score_a = '3'
                                            player_score_b = '2'
                                            break
                                        elif resolved_injury == 'b':
                                            player_score_a = '2'
                                            player_score_b = '3'
                                            break
                                        else:
                                            print("invalid input")
                                else:
                                    print("incorrect input - please now manually enter score one player must reach 3 sets")
                                    print("\n")
                                    print(row['Player A'], row['Score Player A'], row['Player B'], row['Score Player B'])
                                    player_score_a = input(row['Player A'])
                                    player_score_b = input(row['Player B'])
                            else:
                                break
                    elif mensOrWomens == 'LADIES':
                        while True:
                            if (not player_score_a.isdigit() or not player_score_b.isdigit()):
                                print("incorrect input - please only enter integers")
                                print("\n")
                                print(row['Player A']+ " Vs " +row['Player B'])
                                player_score_a = input(row['Player A'])
                                player_score_b = input(row['Player B'])
                            elif (int(player_score_a) >= 3) or (int(player_score_b)>= 3):
                                print("incorrect input - Ladies tournament must be best out of 3")
                                print("\n")
                                print(row['Player A']+ " Vs " +row['Player B'])
                                player_score_a = input(row['Player A'])
                                player_score_b = input(row['Player B'])
                            elif int(player_score_a) == int(player_score_b):
                                print("incorrect input - Ladies tournament can have no draws")
                                print("\n")
                                print(row['Player A']+ " Vs " +row['Player B'])
                                player_score_a = input(row['Player A'])
                                player_score_b = input(row['Player B'])
                            elif int(player_score_a) <= 1 and int(player_score_b)  <= 1:
                                injury = input("This is a incomplete match, was there an injury? Y/N ")
                                print(player_score_a)
                                print(player_score_b)
                                if injury == 'y':
                                    while True :
                                        print("please select a player to go through \n")
                                        print(" press A for player: " + row['Player A']+"\n")
                                        print(" press B for player: " + row['Player B']+"\n")
                                        resolved_injury = input("selection: ")
                                        if resolved_injury == 'a':
                                            player_score_a = '3'
                                            player_score_b = '2'
                                            break
                                        elif resolved_injury == 'b':
                                            player_score_a = '2'
                                            player_score_b = '3'
                                            break
                                        else:
                                            print("invalid input")
                                else:
                                    print("incorrect input - please now manually enter score one player must reach 2 sets")
                                    print("\n")
                                    print(row['Player A'], row['Score Player A'], row['Player B'], row['Score Player B'])
                                    player_score_a = input(row['Player A'])
                                    player_score_b = input(row['Player B'])
                            else:
                                break

                    finished = finished + 1
                    if TournamentRound == 6:
                          if (player_score_a > player_score_b):
                              if (int(player_score_a) - int(player_score_b) == 3)or (mensOrWomens == 'LADIES' and (int(player_score_a) - int(player_score_b) == 2)):
                                  bonusWinMaxPoints.append(row['Player A'])
                              elif (int(player_score_a) - int(player_score_b) == 2):
                                  bonusPointsMin.append(row['Player A'])
                              elif(int(player_score_a) - int(player_score_b) == 1) or (mensOrWomens == 'LADIES' and (int(player_score_a) - int(player_score_b) == 1)):
                                  winByOne.append(row['Player A'])
                              winner.append(row['Player A'])
                          else:
                              if (int(player_score_b) - int(player_score_a) == 3)or (mensOrWomens == 'LADIES' and (int(player_score_b) - int(player_score_a) == 2)):
                                   bonusWinMaxPoints.append(row['Player B'])
                              elif (int(player_score_b) - int(player_score_a) == 2):
                                  bonusPointsMin.append(row['Player B'])
                              elif(int(player_score_b) - int(player_score_a) == 1)or (mensOrWomens == 'LADIES' and (int(player_score_b) - int(player_score_a) == 1)):
                                  winByOne.append(row['Player B'])
                              winner.append(row['Player B'])
                    if (player_score_a < player_score_b):
                          if (int(player_score_b) - int(player_score_a) == 3)or (mensOrWomens == 'LADIES' and (int(player_score_b) - int(player_score_a) == 2)):
                              if TournamentRound < 6:
                                  bonusWinMaxPoints.append(row['Player B'])
                          elif (int(player_score_b) - int(player_score_a) == 2):
                              if TournamentRound < 6:
                                  bonusPointsMin.append(row['Player B'])
                          elif(int(player_score_b) - int(player_score_a) == 1)or (mensOrWomens == 'LADIES' and (int(player_score_b) - int(player_score_a) == 1)):
                                  winByOne.append(row['Player B'])
                          doesNotAdvancedToNextRound.append(row['Player A'])
                          AdvancedToNextRound.append(row['Player B'])
                    if(player_score_a > player_score_b):
                        if (int(player_score_a) - int(player_score_b) == 3) or (mensOrWomens == 'LADIES' and (int(player_score_a) - int(player_score_b) == 2)):
                            if TournamentRound < 6:
                                bonusWinMaxPoints.append(row['Player A'])
                        elif (int(player_score_a) - int(player_score_b) == 2):
                            if TournamentRound < 6:
                                bonusPointsMin.append(row['Player A'])
                        elif(int(player_score_a) - int(player_score_b) == 1)or (mensOrWomens == 'LADIES' and (int(player_score_a) - int(player_score_b) == 1)):
                            if TournamentRound < 6:
                                winByOne.append(row['Player A'])
                        doesNotAdvancedToNextRound.append(row['Player B'])
                        AdvancedToNextRound.append(row['Player A'])
                print("\n")
                for i in doesNotAdvancedToNextRound: # i stands for player A or B
                    finished = int(finished)
                    finished = finished + 1
                    finished = str(finished)
                    roundpoints =  rankings(finished, tournament)
                    prizeMoney = prizeMoneyFromTournament(finished, tournament)
                    if mensOrWomens == 'MEN':
                        for player in maleLeaderBoard:
                            if i == player._name:
                                totalpoints = totalRoundPoints(tournament,roundpoints)
                                player._ranking += totalpoints
                                player._prizeMoney += prizeMoney
                        if tournament == 'TAC1':
                                 for player_ranking_tac1 in tac1_ranking_points_list_mens:
                                    if i == player_ranking_tac1._name:
                                         player_ranking_tac1._prizeMoney += prizeMoney
                                         player_ranking_tac1._ranking += totalpoints
                        if tournament == 'TAE21':
                                for player_ranking_tae21 in tae21_ranking_points_list_mens:
                                    if i == player_ranking_tae21._name:
                                         player_ranking_tae21._prizeMoney += prizeMoney
                                         player_ranking_tae21._ranking += totalpoints
                        if tournament == 'TAW11':
                                for player_ranking_taw11 in taw11_ranking_points_list_mens:
                                    if i == player_ranking_taw11._name:
                                         player_ranking_taw11._prizeMoney += prizeMoney
                                         player_ranking_taw11._ranking += totalpoints
                        if tournament == 'TBS2':
                                for player_ranking_tbs2 in tbs2_ranking_points_list_mens:
                                    if i == player_ranking_tbs2._name:
                                         player_ranking_tbs2._prizeMoney += prizeMoney
                                         player_ranking_tbs2._ranking += totalpoints

                    if mensOrWomens == 'LADIES':
                        for player in femaleLeaderBoard:
                           if i == player._name:
                               totalpoints = totalRoundPoints(tournament,roundpoints)
                               player._ranking += totalpoints
                               player._prizeMoney += prizeMoney
                        if tournament == 'TAC1':
                                 for player_ranking_tac1 in tac1_ranking_points_list_womens:
                                    if i == player_ranking_tac1._name:
                                         player_ranking_tac1._prizeMoney += prizeMoney
                                         player_ranking_tac1._ranking += totalpoints
                        if tournament == 'TAE21':
                                for player_ranking_tae21 in tae21_ranking_points_list_womens:
                                    if i == player_ranking_tae21._name:
                                         player_ranking_tae21._prizeMoney += prizeMoney
                                         player_ranking_tac1._ranking += totalpoints
                        if tournament == 'TAW11':
                                for player_ranking_taw11 in taw11_ranking_points_list_womens:
                                    if i == player_ranking_taw11._name:
                                         player_ranking_taw11._prizeMoney += prizeMoney
                                         player_ranking_tac1._ranking += totalpoints
                        if tournament == 'TBS2':
                                for player_ranking_tbs2 in tbs2_ranking_points_list_womens:
                                    if i == player_ranking_tbs2._name:
                                         player_ranking_tbs2._prizeMoney += prizeMoney
                                         player_ranking_tac1._ranking += totalpoints
                    if mensOrWomens == 'MEN':
                        for playerdataAll in malePlayerNamesDatatableAll:
                                if i == playerdataAll._player:
                                    playerdataAll._losses+= 1
                        if tournament == 'TAC1':
                            for playerdataTac1 in malePlayerNamesDatatableTac1:
                                if i == playerdataTac1._player:
                                    playerdataTac1._losses+= 1
                        elif tournament == 'TAE21':
                            for playerdataTae21 in malePlayerNamesDatatableTae21:
                                if i == playerdataTae21._player:
                                    playerdataTae21._losses+= 1
                        elif tournament == 'TAW11':
                            for playerdataTaw11 in malePlayerNamesDatatableTaw11:
                                if i == playerdataTaw11._player:
                                    playerdataTaw11._losses+= 1
                        elif tournament == 'TBS2':
                            for playerdataTbs2 in malePlayerNamesDatatableTbs2:
                                if i == playerdataTbs2._player:
                                    playerdataTbs2._losses+= 1
                    elif mensOrWomens == 'LADIES':
                        for playerdataLadiesAll in femalePlayerNamesDatatableAll:
                                if i == playerdataLadiesAll._player:
                                    playerdataLadiesAll._losses+= 1
                        if tournament == 'TAC1':
                            for playerdataTac1 in femalePlayerNamesDatatableTac1:
                                if i == playerdataTac1._player:
                                    playerdataTac1._losses+= 1
                        elif tournament == 'TAE21':
                            for playerdataTae21 in femalePlayerNamesDatatableTae21:
                                if i == playerdataTae21._player:
                                    playerdataTae21._losses+= 1
                        elif tournament == 'TAW11':
                            for playerdataTaw11 in femalePlayerNamesDatatableTaw11:
                                if i == playerdataTaw11._player:
                                    playerdataTaw11._losses+= 1
                        elif tournament == 'TBS2':
                            for playerdataTbs2 in femalePlayerNamesDatatableTbs2:
                                if i == playerdataTbs2._player:
                                    playerdataTbs2._losses+= 1
                for i in winner: # i stands for player player A or B
                    finished = int(finished)
                    finished = finished - 1
                    finished = str(finished)
                    roundpoints =  rankings(finished,tournament)
                    prizeMoney = prizeMoneyFromTournament(finished, tournament)
                    if mensOrWomens == 'MEN':
                        for player in maleLeaderBoard:
                            if i == player._name:
                                totalpoints = totalRoundPoints(tournament,roundpoints)
                                player._ranking += totalpoints
                                player._prizeMoney += prizeMoney
                        if tournament == 'TAC1':
                                for player_ranking_tac1 in tac1_ranking_points_list_mens:
                                    if i == player_ranking_tac1._name:
                                         player_ranking_tac1._prizeMoney += prizeMoney
                                         player_ranking_tac1._ranking += totalpoints
                        if tournament == 'TAE21':
                                for player_ranking_tae21 in tae21_ranking_points_list_mens:
                                    if i == player_ranking_tae21._name:
                                         player_ranking_tae21._prizeMoney += prizeMoney
                                         player_ranking_tae21._ranking += totalpoints
                        if tournament == 'TAW11':
                                for player_ranking_taw11 in taw11_ranking_points_list_mens:
                                    if i == player_ranking_taw11._name:
                                         player_ranking_taw11._prizeMoney += prizeMoney
                                         player_ranking_taw11._ranking += totalpoints
                        if tournament == 'TBS2':
                                for player_ranking_tbs2 in tbs2_ranking_points_list_mens:
                                    if i == player_ranking_tbs2._name:
                                         player_ranking_tbs2._prizeMoney += prizeMoney
                                         player_ranking_tbs2._ranking += totalpoints
                    if mensOrWomens == 'LADIES':
                        for player in femaleLeaderBoard:
                            if i == player._name:
                                totalpoints = totalRoundPoints(tournament,roundpoints)
                                player._ranking += totalpoints
                                player._prizeMoney += prizeMoney
                        if tournament == 'TAC1':
                                 for player_ranking_tac1 in tac1_ranking_points_list_womens:
                                    if i == player_ranking_tac1._name:
                                         player_ranking_tac1._prizeMoney += prizeMoney
                                         player_ranking_tac1._ranking += totalpoints
                        if tournament == 'TAE21':
                                for player_ranking_tae21 in tae21_ranking_points_list_womens:
                                    if i == player_ranking_tae21._name:
                                         player_ranking_tae21._prizeMoney += prizeMoney
                                         player_ranking_tae21._ranking += totalpoints

                        if tournament == 'TAW11':
                                for player_ranking_taw11 in taw11_ranking_points_list_womens:
                                    if i == player_ranking_taw11._name:
                                         player_ranking_taw11._prizeMoney += prizeMoney
                                         player_ranking_taw11._ranking += totalpoints
                        if tournament == 'TBS2':
                                for player_ranking_tbs2 in tbs2_ranking_points_list_womens:
                                    if i == player_ranking_tbs2._name:
                                         player_ranking_tbs2._prizeMoney += prizeMoney
                                         player_ranking_tbs2._ranking += totalpoints
                for i in bonusWinMaxPoints:
                    if mensOrWomens == 'MEN':
                        for player in maleLeaderBoard:
                             if i == player._name:
                                thebonus = bonusPointsMaxMethod(roundpoints)
                                thebonus = totalRoundPoints(tournament,thebonus)
                                thebonus = round(thebonus,2)
                                print(player._name + " gained a bouns  of :" + str(thebonus))
                                player._ranking += thebonus
                                if tournament == 'TAC1':
                                     for player_ranking_tac1 in tac1_ranking_points_list_mens:
                                        if i == player_ranking_tac1._name:
                                             player_ranking_tac1._ranking += thebonus
                                if tournament == 'TAE21':
                                    for player_ranking_tae21 in tae21_ranking_points_list_mens:
                                        if i == player_ranking_tae21._name:
                                             player_ranking_tae21._ranking += thebonus
                                if tournament == 'TAW11':
                                    for player_ranking_taw11 in taw11_ranking_points_list_mens:
                                        if i == player_ranking_taw11._name:
                                             player_ranking_taw11._ranking +=thebonus
                                if tournament == 'TBS2':
                                    for player_ranking_tbs2 in tbs2_ranking_points_list_mens:
                                        if i == player_ranking_tbs2._name:
                                             player_ranking_tbs2._ranking += thebonus
                                if TournamentRound == 6:
                                    player._ranking =  player._ranking - totalpoints
                                    if tournament == 'TAC1':
                                         for player_ranking_tac1 in tac1_ranking_points_list_mens:
                                            if i == player_ranking_tac1._name:
                                                 player_ranking_tac1._ranking += player_ranking_tac1._ranking - totalpoints
                                    if tournament == 'TAE21':
                                        for player_ranking_tae21 in tae21_ranking_points_list_mens:
                                            if i == player_ranking_tae21._name:
                                                 player_ranking_tae21._ranking += player_ranking_tae21._ranking - totalpoints
                                    if tournament == 'TAW11':
                                        for player_ranking_taw11 in taw11_ranking_points_list_mens:
                                            if i == player_ranking_taw11._name:
                                                 player_ranking_taw11._ranking += player_ranking_taw11 - totalpoints
                                    if tournament == 'TBS2':
                                        for player_ranking_tbs2 in tbs2_ranking_points_list_mens:
                                            if i == player_ranking_tbs2._name:
                                                 player_ranking_tbs2._ranking += player_ranking_tbs2 - totalpoints
                        if mensOrWomens == 'MEN':
                            for playerdataAll in malePlayerNamesDatatableAll:
                                if i == playerdataAll._player:
                                    playerdataAll._win_by_three+= 1
                            if tournament == 'TAC1':
                                for playerdataTac1 in malePlayerNamesDatatableTac1:
                                    if i == playerdataTac1._player:
                                        playerdataTac1._win_by_three += 1
                            elif tournament == 'TAE21':
                                for playerdataTae21 in malePlayerNamesDatatableTae21:
                                    if i == playerdataTae21._player:
                                        playerdataTae21._win_by_three+= 1
                            elif tournament == 'TAW11':
                                for playerdataTaw11 in malePlayerNamesDatatableTaw11:
                                    if i == playerdataTaw11._player:
                                        playerdataTaw11._win_by_three+= 1
                            elif tournament == 'TBS2':
                                for playerdataTbs2 in malePlayerNamesDatatableTbs2:
                                    if i == playerdataTbs2._player:
                                        playerdataTbs2._win_by_three+= 1
                    if mensOrWomens == 'LADIES':
                        for player in femaleLeaderBoard:
                            if i == player._name:
                                thebonus = bonusPointsMaxMethod(roundpoints)
                                thebonus = totalRoundPoints(tournament,thebonus)
                                thebonus = round(thebonus,2)
                                print(player._name + " gained a bouns  of :" + str(thebonus))
                                player._ranking += thebonus
                                if tournament == 'TAC1':
                                     for player_ranking_tac1 in tac1_ranking_points_list_womens:
                                        if i == player_ranking_tac1._name:
                                             player_ranking_tac1._ranking += thebonus
                                if tournament == 'TAE21':
                                    for player_ranking_tae21 in tae21_ranking_points_list_womens:
                                        if i == player_ranking_tae21._name:
                                             player_ranking_tae21._ranking += thebonus
                                if tournament == 'TAW11':
                                    for player_ranking_taw11 in taw11_ranking_points_list_womens:
                                        if i == player_ranking_taw11._name:
                                             player_ranking_taw11._ranking +=thebonus
                                if tournament == 'TBS2':
                                    for player_ranking_tbs2 in tbs2_ranking_points_list_womens:
                                        if i == player_ranking_tbs2._name:
                                             player_ranking_tbs2._ranking += thebonus
                                if TournamentRound == 6:
                                    player._ranking =  player._ranking - totalpoints
                                    if tournament == 'TAC1':
                                         for player_ranking_tac1 in tac1_ranking_points_list_womens:
                                            if i == player_ranking_tac1._name:
                                                 player_ranking_tac1._ranking += player_ranking_tac1._ranking - totalpoints
                                                 print(player_ranking_tac1._ranking)
                                                 print(thebonus)
                                    if tournament == 'TAE21':
                                        for player_ranking_tae21 in tae21_ranking_points_list_womens:
                                            if i == player_ranking_tae21._name:
                                                 player_ranking_tae21._ranking += player_ranking_tae21._ranking - totalpoints
                                    if tournament == 'TAW11':
                                        for player_ranking_taw11 in taw11_ranking_points_list_womens:
                                            if i == player_ranking_taw11._name:
                                                 player_ranking_taw11._ranking += player_ranking_taw11 - totalpoints
                                    if tournament == 'TBS2':
                                        for player_ranking_tbs2 in tbs2_ranking_points_list_womens:
                                            if i == player_ranking_tbs2._name:
                                                 player_ranking_tbs2._ranking += player_ranking_tbs2 - totalpoints
                        if mensOrWomens == 'LADIES':
                            for playerdataLadiesAll in femalePlayerNamesDatatableAll:
                                if i == playerdataLadiesAll._player:
                                    playerdataLadiesAll._win_by_three+= 1
                            if tournament == 'TAC1':
                                for playerdataTac1 in femalePlayerNamesDatatableTac1:
                                    if i == playerdataTac1._player:
                                        playerdataTac1._win_by_three+= 1
                            elif tournament == 'TAE21':
                                for playerdataTae21 in femalePlayerNamesDatatableTae21:
                                    if i == playerdataTae21._player:
                                        playerdataTae21._win_by_three+= 1
                            elif tournament == 'TAW11':
                                for playerdataTaw11 in femalePlayerNamesDatatableTaw11:
                                    if i == playerdataTaw11._player:
                                        playerdataTaw11._win_by_three+= 1
                            elif tournament == 'TBS2':
                                for playerdataTbs2 in femalePlayerNamesDatatableTbs2:
                                    if i == playerdataTbs2._player:
                                        playerdataTbs2._win_by_three+= 1
                for i in bonusPointsMin:
                    for player in maleLeaderBoard:
                        if i == player._name:
                            thebonus = bonusPointsMinMethod(roundpoints)
                            thebonus = totalRoundPoints(tournament,thebonus)
                            thebonus = round(thebonus,2)
                            print(player._name + " gained a bouns  of :" + str(thebonus))
                            player._ranking += thebonus
                            if tournament == 'TAC1':
                                 for player_ranking_tac1 in tac1_ranking_points_list_mens:
                                    if i == player_ranking_tac1._name:
                                         player_ranking_tac1._ranking += thebonus
                            if tournament == 'TAE21':
                                for player_ranking_tae21 in tae21_ranking_points_list_mens:
                                    if i == player_ranking_tae21._name:
                                         player_ranking_tae21._ranking += thebonus
                            if tournament == 'TAW11':
                                for player_ranking_taw11 in taw11_ranking_points_list_mens:
                                    if i == player_ranking_taw11._name:
                                         player_ranking_taw11._ranking +=thebonus
                            if tournament == 'TBS2':
                                for player_ranking_tbs2 in tbs2_ranking_points_list_mens:
                                    if i == player_ranking_tbs2._name:
                                         player_ranking_tbs2._ranking += thebonus
                    for playerdataAll in malePlayerNamesDatatableAll:
                                if i == playerdataAll._player:
                                    playerdataAll._win_by_two+= 1
                    if tournament == 'TAC1':
                        for playerdataTac1 in malePlayerNamesDatatableTac1:
                            if i == playerdataTac1._player:
                                playerdataTac1._win_by_two += 1
                    elif tournament == 'TAE21':
                        for playerdataTae21 in malePlayerNamesDatatableTae21:
                            if i == playerdataTae21._player:
                                playerdataTae21._win_by_two+= 1
                    elif tournament == 'TAW11':
                        for playerdataTaw11 in malePlayerNamesDatatableTaw11:
                            if i == playerdataTaw11._player:
                                playerdataTaw11._win_by_two+= 1
                    elif tournament == 'TBS2':
                        for playerdataTbs2 in malePlayerNamesDatatableTbs2:
                            if i == playerdataTbs2._player:
                                playerdataTbs2._win_by_two+= 1

                for i in AdvancedToNextRound:
                    if mensOrWomens == 'MEN':
                        for playerdataAll in malePlayerNamesDatatableAll:
                                if i == playerdataAll._player:
                                    playerdataAll._wins+= 1
                        if tournament == 'TAC1':
                            for playerdataTac1 in malePlayerNamesDatatableTac1:
                                if i == playerdataTac1._player:
                                     playerdataTac1._wins += 1
                        elif tournament == 'TAE21':
                            for playerdataTae21 in malePlayerNamesDatatableTae21:
                                if i == playerdataTae21._player:
                                    playerdataTae21._wins += 1
                        elif tournament == 'TAW11':
                            for playerdataTaw11 in malePlayerNamesDatatableTaw11:
                                if i == playerdataTaw11._player:
                                    playerdataTaw11._wins+= 1
                        elif tournament == 'TBS2':
                            for playerdataTbs2 in malePlayerNamesDatatableTbs2:
                                if i == playerdataTbs2._player:
                                    playerdataTbs2._wins+= 1
                    elif mensOrWomens == 'LADIES':
                        for playerdataLadiesAll in femalePlayerNamesDatatableAll:
                                if i == playerdataLadiesAll._player:
                                    playerdataLadiesAll._wins+= 1
                        if tournament == 'TAC1':
                            for playerdataTac1 in femalePlayerNamesDatatableTac1:
                                if i == playerdataTac1._player:
                                    playerdataTac1._wins+= 1
                        elif tournament == 'TAE21':
                            for playerdataTae21 in femalePlayerNamesDatatableTae21:
                                if i == playerdataTae21._player:
                                    playerdataTae21._wins+= 1
                        elif tournament == 'TAW11':
                            for playerdataTaw11 in femalePlayerNamesDatatableTaw11:
                                if i == playerdataTaw11._player:
                                    playerdataTaw11._wins+= 1
                        elif tournament == 'TBS2':
                            for playerdataTbs2 in femalePlayerNamesDatatableTbs2:
                                if i == playerdataTbs2._player:
                                    playerdataTbs2._wins+= 1
                for i in winByOne:
                    if mensOrWomens == 'MEN':
                        for playerdataAll in malePlayerNamesDatatableAll:
                                if i == playerdataAll._player:
                                    playerdataAll._win_by_one+= 1
                        if tournament == 'TAC1':
                            for playerdataTac1 in malePlayerNamesDatatableTac1:
                                if i == playerdataTac1._player:
                                     playerdataTac1._win_by_one += 1
                        elif tournament == 'TAE21':
                            for playerdataTae21 in malePlayerNamesDatatableTae21:
                                if i == playerdataTae21._player:
                                    playerdataTae21._win_by_one += 1
                        elif tournament == 'TAW11':
                            for playerdataTaw11 in malePlayerNamesDatatableTaw11:
                                if i == playerdataTaw11._player:
                                    playerdataTaw11._win_by_one+= 1
                        elif tournament == 'TBS2':
                            for playerdataTbs2 in malePlayerNamesDatatableTbs2:
                                if i == playerdataTbs2._player:
                                    playerdataTbs2._win_by_one+= 1
                    elif mensOrWomens == 'LADIES':
                        for playerdataLadiesAll in femalePlayerNamesDatatableAll:
                                if i == playerdataLadiesAll._player:
                                    playerdataLadiesAll._win_by_one+= 1
                        if tournament == 'TAC1':
                            for playerdataTac1 in femalePlayerNamesDatatableTac1:
                                if i == playerdataTac1._player:
                                    playerdataTac1._win_by_one+= 1
                        elif tournament == 'TAE21':
                            for playerdataTae21 in femalePlayerNamesDatatableTae21:
                                if i == playerdataTae21._player:
                                    playerdataTae21._win_by_one+= 1
                        elif tournament == 'TAW11':
                            for playerdataTaw11 in femalePlayerNamesDatatableTaw11:
                                if i == playerdataTaw11._player:
                                    playerdataTaw11._win_by_one+= 1
                        elif tournament == 'TBS2':
                            for playerdataTbs2 in femalePlayerNamesDatatableTbs2:
                                if i == playerdataTbs2._player:
                                    playerdataTbs2._win_by_one+= 1
#Description: processes the selected tournament (1st arg) and gender (2nd arg) by CSV input
#and gives corresponding ranking points and prize money to player object
#parameters: tournament - String, mensOrWomens - String
#return type: none
#Description: main menu takes inputs, which then are linked to corresponding functions
#parameters: none
#return type: none
def menu():
    while True:
        print("---------------------------------------------------------------------------")
        print("Menu")
        print("---------------------------------------------------------------------------")
        print("0: Exit System\n")
        print("1: View Players\n")
        print("2: View Rankings\n")
        print("3: print stats\n")
        print("4: Tournaments via Manual Input\n")
        print("5: Save Progress\n")
        print("6: Load Previous Saved Data \n")
        print("7: Delete saved data \n")
        print("8: Continue tourny\n")
        menuInput = input('Enter a number 0-7: ')
        menuInput = menuInput.strip()
        if menuInput == '1':
            listPlayers()
        elif menuInput == '2':
            viewRankings()
        elif menuInput == '3':
            statsSelection()

        elif menuInput == '4':
            tournamentsViaManualInput()
        elif menuInput == '5':
            print("Data saved")
            maleSavedprogress()
            femaleSavedprogress()
        elif menuInput == '6':
            PreviousSavedData()
            print("Data Loaded")
            menu()
        elif menuInput == '7':
            deleteSavedData()
            print("Data Deleted")
            menu()
        elif menuInput == '8':
             with open('ROUND PROGRESS.csv', newline='') as csvfile:
                    reader = csv.DictReader(csvfile)
                    for row in reader:
                        print(row['ROUND'], row['TOURNAMENT'], row['GENDER'])
                        TournamentRound = row['ROUND']
                        tournament = row['TOURNAMENT']
                        mensOrWomens = row['GENDER']
                        TournamentRound = int(TournamentRound)
                        TournamentRound = (TournamentRound+1)
                        tennisRound(tournament,mensOrWomens,TournamentRound)
        elif menuInput == '0':
            print("Goodbaye, have a nice day!")
            sys.exit()
        else:
            print("Invalid input, try again\n")
#Description: Saves male leaderboard
#parameters: none
#return type: none
def maleSavedprogress():
    with open('MALE SAVE PROGRESS.csv', 'w', newline='') as csvfile:
        fieldnames = ['first name', 'Rankings','Prize money']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for player in maleLeaderBoard:
            writer.writerow({'first name': player._name, 'Rankings': str(player._ranking),'Prize money': str(player._prizeMoney)})
#Description: Saves female leaderboard
#parameters: none
#return type: none
def femaleSavedprogress():
    with open('FEMALE SAVE PROGRESS.csv', 'w', newline='') as csvfile:
        fieldnames = ['first name', 'Rankings','Prize money']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for player in femaleLeaderBoard:
            writer.writerow({'first name': player._name, 'Rankings': str(player._ranking),'Prize money': str(player._prizeMoney)})
#Description: scans CSV file for saved male/female leaderboards, then assigns points to players
#parameters: none
#return type: none
def PreviousSavedData():
     with open('FEMALE SAVE PROGRESS.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                for player in femaleLeaderBoard:
                    if row['first name'] == player._name:
                        print(row['first name'], row['Rankings'], row['Prize money'])
                        currentRanking = row['Rankings']
                        currentPrizeMoney = row['Prize money']
                        player._ranking = float(currentRanking)
                        player._prizeMoney = float(currentPrizeMoney)
     with open('MALE SAVE PROGRESS.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                for player in maleLeaderBoard:
                    if row['first name'] == player._name:
                        print(row['first name'], row['Rankings'], row['Prize money'])
                        currentRanking = row['Rankings']
                        currentPrizeMoney = row['Prize money']
                        player._ranking = float(currentRanking)
                        player._prizeMoney = float(currentPrizeMoney)
def deleteSavedData():
     with open('FEMALE SAVE PROGRESS.csv', 'w', newline='') as csvfile:
        fieldnames = ['first name', 'Rankings','Prize money']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for player in femaleLeaderBoard:
            writer.writerow({'first name': player._name, 'Rankings': str(0.0),'Prize money': str(0)})
     with open('MALE SAVE PROGRESS.csv', 'w', newline='') as csvfile:
        fieldnames = ['first name', 'Rankings','Prize money']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for player in maleLeaderBoard:
            writer.writerow({'first name': player._name, 'Rankings': str(0.0),'Prize money': str(0)})
# stats menus handles selction from user
def statsSelection():
    with open('TOURNAMENT NAME.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        tournamentNames = []
        for row in reader:
            tournamentNames.append(row['Tournament'])
    genderMenuInput = input('Enter M for Male tournaments or F for Female tournaments: ')
    genderMenuInput = genderMenuInput.strip()
    genderMenuInput = genderMenuInput.upper()
    if genderMenuInput == 'M':
        mensOrWomens = 'MEN'
    elif genderMenuInput == 'F':
        mensOrWomens = 'LADIES'
    else:
        print("not a valid input")
        tournamentsViaManualInput()
    print('Tournaments')
    print('1.'+tournamentNames[0]+'\n')
    print('2.'+tournamentNames[1]+'\n')
    print('3.'+tournamentNames[2]+'\n')
    print('4.'+tournamentNames[3]+'\n')
    print('5. All Tournaments \n')
    tournamentMenuInput = input('Enter a number 1-5: ')
    tournamentMenuInput = tournamentMenuInput.strip()
    if tournamentMenuInput == '1':
        tournament = tournamentNames[0]
        Stats(tournament,mensOrWomens)
    elif tournamentMenuInput == '2':
        tournament = tournamentNames[1]
        Stats(tournament,mensOrWomens)
    elif tournamentMenuInput == '3':
        tournament = tournamentNames[2]
        Stats(tournament,mensOrWomens)
    elif tournamentMenuInput == '4':
        tournament = tournamentNames[3]
        Stats(tournament,mensOrWomens)
    elif tournamentMenuInput == '5':
        tournament = 'ALL'
        Stats(tournament,mensOrWomens)
    else:
        print('Invalid input, try again')
        statsSelection()
def Stats(tournament,mensOrWomens):
            if tournament == 'TAC1':
                if mensOrWomens == 'MEN':
                    printMensStatsoptions()
                    tac1mensStatsMenuInput = input('Enter a number 1-5: ')
                    if tac1mensStatsMenuInput == '1':
                        print("Mens TAC1 Win Stats")
                        malePlayerNamesDatatableTac1.sort(key = lambda playerdata: playerdata._wins, reverse=True)
                        for playerdata in malePlayerNamesDatatableTac1:
                            print(playerdata._player+ " number of wins: " +str(playerdata._wins) )
                    if tac1mensStatsMenuInput == '2':
                        print("Mens TAC1 Win by 3 Stats")
                        malePlayerNamesDatatableTac1.sort(key = lambda playerdata: playerdata._win_by_three, reverse=True)
                        for playerdata in malePlayerNamesDatatableTac1:
                            print(playerdata._player+ " number of 3-0 wins: " +str(playerdata._win_by_three))
                    if tac1mensStatsMenuInput == '3':
                        print("Mens TAC1 Win by 2 Sets Stats")
                        malePlayerNamesDatatableTac1.sort(key = lambda playerdata: playerdata._win_by_two, reverse=True)
                        for playerdata in malePlayerNamesDatatableTac1:
                            print(playerdata._player+ " number of 3-1 wins: " +str(playerdata._win_by_two))
                    if tac1mensStatsMenuInput == '4':
                        print("Mens TAC1 Win by 1 Set Stats")
                        malePlayerNamesDatatableTac1.sort(key = lambda playerdata: playerdata._win_by_one, reverse=True)
                        for playerdata in malePlayerNamesDatatableTac1:
                            print(playerdata._player+ " number of 3-2 wins: " +str(playerdata._win_by_one))
                    if tac1mensStatsMenuInput == '5':
                        print("Mens TAC1 losses Stats")
                        malePlayerNamesDatatableTac1.sort(key = lambda playerdata: playerdata._losses, reverse=True)
                        for playerdata in malePlayerNamesDatatableTac1:
                            print(playerdata._player+ " number of losses: " +str(playerdata._losses))
                    if tac1mensStatsMenuInput == '6':
                        print("Mens TAW11 percenatge Stats")
                        malePlayerNamesDatatableTac1.sort(key = lambda playerdata: playerdata._wins, reverse=True)
                        for playerdata in malePlayerNamesDatatableTac1:
                            percent = percentageCal(playerdata._wins,playerdata._losses)
                            print(playerdata._player+" win : %"+str(percent))
                    if tac1mensStatsMenuInput == '7':
                        print("Mens TAC1 Stats")
                        malePlayerNamesDatatableTac1.sort(key = lambda playerdata: playerdata._wins, reverse=True)
                        for playerdata in malePlayerNamesDatatableTac1:
                            percent = percentageCal(playerdata._wins,playerdata._losses)
                            print(playerdata._player+" Wins: "+str(playerdata._wins)+" 3-0 wins: "+str(playerdata._win_by_three)+" 3-1 wins: "+str(playerdata._win_by_two)+" 3-2 wins: "+str(playerdata._win_by_one)+" losses: "+str(playerdata._losses)+" win percentage : %"+str(percent))
                elif mensOrWomens == 'LADIES':
                    printLadiesStatsoptions()
                    tac1womensStatsMenuInput = input('Enter a number 1-5: ')
                    if tac1womensStatsMenuInput == '1':
                        print("Ladies TAC1 Win Stats")
                        femalePlayerNamesDatatableTac1.sort(key = lambda playerdata: playerdata._wins, reverse=True)
                        for playerdata in femalePlayerNamesDatatableTac1:
                            print(playerdata._player+ " number of wins: " +str(playerdata._wins) )
                    if tac1womensStatsMenuInput == '2':
                        print("Ladies TAC1 2-0 Stats")
                        femalePlayerNamesDatatableTac1.sort(key = lambda playerdata: playerdata._win_by_three, reverse=True)
                        for playerdata in femalePlayerNamesDatatableTac1:
                            print(playerdata._player+ " number of 2-0 wins: " +str(playerdata._win_by_three))
                    if tac1womensStatsMenuInput == '3':
                        print("Ladies TAC1 2-1 Stats")
                        femalePlayerNamesDatatableTac1.sort(key = lambda playerdata: playerdata._win_by_one, reverse=True)
                        for playerdata in femalePlayerNamesDatatableTac1:
                            print(playerdata._player+ " number of 2-1 wins: " +str(playerdata._win_by_one))
                    if tac1womensStatsMenuInput == '4':
                        print("Ladies TAC1 losses Stats")
                        femalePlayerNamesDatatableTac1.sort(key = lambda playerdata: playerdata._losses, reverse=True)
                        for playerdata in femalePlayerNamesDatatableTac1:
                            print(playerdata._player+ " number of losses: " +str(playerdata._losses))
                    if tac1womensStatsMenuInput == '5':
                        print("Ladies TAC1 percenatge Stats")
                        femalePlayerNamesDatatableTac1.sort(key = lambda playerdata: playerdata._wins, reverse=True)
                        for playerdata in femalePlayerNamesDatatableTac1:
                            percent = percentageCal(playerdata._wins,playerdata._losses)
                            print(playerdata._player+" win : %"+str(percent))
                    if tac1womensStatsMenuInput == '6':
                        print("Ladies TAC1 Stats")
                        femalePlayerNamesDatatableTac1.sort(key = lambda playerdata: playerdata._wins, reverse=True)
                        for playerdata in femalePlayerNamesDatatableTac1:
                            percent = percentageCal(playerdata._wins,playerdata._losses)
                            print(playerdata._player+" Wins: "+str(playerdata._wins)+" 2-0 wins: "+str(playerdata._win_by_three)+" 2-1 wins: "+str(playerdata._win_by_one)+" losses: "+str(playerdata._losses)+" win percentage: %"+str(percent))
            elif tournament == 'TAE21':
                if mensOrWomens == 'MEN':
                    printMensStatsoptions()
                    tae21mensStatsMenuInput = input('Enter a number 1-5: ')
                    if tae21mensStatsMenuInput == '1':
                        print("Mens TAE21 Win Stats")
                        malePlayerNamesDatatableTae21.sort(key = lambda playerdata: playerdata._wins, reverse=True)
                        for playerdata in malePlayerNamesDatatableTae21:
                            print(playerdata._player+ " number of wins: " +str(playerdata._wins) )
                    if tae21mensStatsMenuInput == '2':
                        print("Mens TAE21 3-0 Stats")
                        malePlayerNamesDatatableTae21.sort(key = lambda playerdata: playerdata._win_by_three, reverse=True)
                        for playerdata in malePlayerNamesDatatableTae21:
                            print(playerdata._player+ " number of 3-0 wins: " +str(playerdata._win_by_three))
                    if tae21mensStatsMenuInput == '3':
                        print("Mens TAE21 3-1 Stats")
                        malePlayerNamesDatatableTae21.sort(key = lambda playerdata: playerdata._win_by_two, reverse=True)
                        for playerdata in malePlayerNamesDatatableTae21:
                            print(playerdata._player+ " number of 3-1 wins: " +str(playerdata._win_by_two))
                    if tae21mensStatsMenuInput == '4':
                        print("Mens TAE21 3-2 Stats")
                        malePlayerNamesDatatableTae21.sort(key = lambda playerdata: playerdata._win_by_one, reverse=True)
                        for playerdata in malePlayerNamesDatatableTae21:
                            print(playerdata._player+ " number of 3-2 wins: " +str(playerdata._win_by_one))
                    if tae21mensStatsMenuInput == '5':
                        print("Mens TAE21 losses Stats")
                        malePlayerNamesDatatableTae21.sort(key = lambda playerdata: playerdata._losses, reverse=True)
                        for playerdata in malePlayerNamesDatatableTae21:
                            print(playerdata._player+ " number of losses: " +str(playerdata._losses))
                    if tae21mensStatsMenuInput == '6':
                        print("Mens TAW11 percenatge Stats")
                        malePlayerNamesDatatableTae21.sort(key = lambda playerdata: playerdata._wins, reverse=True)
                        for playerdata in malePlayerNamesDatatableTae21:
                            percent = percentageCal(playerdata._wins,playerdata._losses)
                            print(playerdata._player+" win : %"+str(percent))
                    if tae21mensStatsMenuInput == '7':
                        print("Mens TAE21 Stats")
                        malePlayerNamesDatatableTae21.sort(key = lambda playerdata: playerdata._wins, reverse=True)
                        for playerdata in malePlayerNamesDatatableTae21:
                            percent = percentageCal(playerdata._wins,playerdata._losses)
                            print(playerdata._player+" Wins: "+str(playerdata._wins)+" 3-0 wins: "+str(playerdata._win_by_three)+" 3-1 wins: "+str(playerdata._win_by_two)+" 3-2 wins: "+str(playerdata._win_by_one)+" losses: "+str(playerdata._losses)+" win percentage : %"+str(percent))
                if mensOrWomens == 'LADIES':
                    printLadiesStatsoptions()
                    tae21womensStatsMenuInput = input('Enter a number 1-5: ')
                    if tae21womensStatsMenuInput == '1':
                        print("Ladies TAE21 Win Stats")
                        femalePlayerNamesDatatableTae21.sort(key = lambda playerdata: playerdata._wins, reverse=True)
                        for playerdata in femalePlayerNamesDatatableTae21:
                            print(playerdata._player+ " number of wins: " +str(playerdata._wins) )
                    if tae21womensStatsMenuInput == '2':
                        print("Ladies TAE21 2-0 Stats")
                        femalePlayerNamesDatatableTae21.sort(key = lambda playerdata: playerdata._win_by_three, reverse=True)
                        for playerdata in femalePlayerNamesDatatableTae21:
                            print(playerdata._player+ " number of 2-0 wins: " +str(playerdata._win_by_three))
                    if tae21womensStatsMenuInput == '3':
                        print("Ladies TAE21 2-1 Stats")
                        femalePlayerNamesDatatableTae21.sort(key = lambda playerdata: playerdata._win_by_one, reverse=True)
                        for playerdata in femalePlayerNamesDatatableTae21:
                            print(playerdata._player+ " number of 2-1 wins: " +str(playerdata._win_by_one))
                    if tae21womensStatsMenuInput == '4':
                        print("Ladies TAE21 losses Stats")
                        femalePlayerNamesDatatableTae21.sort(key = lambda playerdata: playerdata._losses, reverse=True)
                        for playerdata in femalePlayerNamesDatatableTae21:
                            print(playerdata._player+ " number of losses: " +str(playerdata._losses))
                    if tae21womensStatsMenuInput == '5':
                        print("Ladies TAE21 percenatge Stats")
                        femalePlayerNamesDatatableTae21.sort(key = lambda playerdata: playerdata._wins, reverse=True)
                        for playerdata in femalePlayerNamesDatatableTae21:
                            percent = percentageCal(playerdata._wins,playerdata._losses)
                            print(playerdata._player+" win : %"+str(percent))
                    if tae21womensStatsMenuInput == '6':
                        print("Ladies TAE21 Stats")
                        femalePlayerNamesDatatableTae21.sort(key = lambda playerdata: playerdata._wins, reverse=True)
                        for playerdata in femalePlayerNamesDatatableTae21:
                            percent = percentageCal(playerdata._wins,playerdata._losses)
                            print(playerdata._player+" Wins: "+str(playerdata._wins)+" 2-0 wins: "+str(playerdata._win_by_three)+" 2-1 wins: "+str(playerdata._win_by_one)+" losses: "+str(playerdata._losses)+" win percentage: %"+str(percent))
            elif tournament == 'TAW11':
                if mensOrWomens == 'MEN':
                    printMensStatsoptions()
                    taw11mensStatsMenuInput = input('Enter a number 1-5: ')
                    if taw11mensStatsMenuInput == '1':
                        print("Mens TAW11 Win Stats")
                        malePlayerNamesDatatableTaw11.sort(key = lambda playerdata: playerdata._wins, reverse=True)
                        for playerdata in malePlayerNamesDatatableTaw11:
                            print(playerdata._player+ " number of wins: " +str(playerdata._wins) )
                    if taw11mensStatsMenuInput == '2':
                        print("Mens TAW11 3-0 Stats")
                        malePlayerNamesDatatableTaw11.sort(key = lambda playerdata: playerdata._win_by_three, reverse=True)
                        for playerdata in malePlayerNamesDatatableTaw11:
                            print(playerdata._player+ " number of 3-0 wins: " +str(playerdata._win_by_three))
                    if taw11mensStatsMenuInput == '3':
                        print("Mens TAW11 3-1 Stats")
                        malePlayerNamesDatatableTaw11.sort(key = lambda playerdata: playerdata._win_by_two, reverse=True)
                        for playerdata in malePlayerNamesDatatableTaw11:
                            print(playerdata._player+ " number of 3-1 wins: " +str(playerdata._win_by_two))
                    if taw11mensStatsMenuInput == '4':
                        print("Mens TAW11 3-2 Stats")
                        malePlayerNamesDatatableTaw11.sort(key = lambda playerdata: playerdata._win_by_one, reverse=True)
                        for playerdata in malePlayerNamesDatatableTaw11:
                            print(playerdata._player+ " number of 3-2 wins: " +str(playerdata._win_by_one))
                    if taw11mensStatsMenuInput == '5':
                        print("Mens TAW11 losses Stats")
                        malePlayerNamesDatatableTaw11.sort(key = lambda playerdata: playerdata._losses, reverse=True)
                        for playerdata in malePlayerNamesDatatableTaw11:
                            print(playerdata._player+ " number of losses: " +str(playerdata._losses))
                    if taw11mensStatsMenuInput == '6':
                        print("Mens TAW11 percenatge Stats")
                        malePlayerNamesDatatableTaw11.sort(key = lambda playerdata: playerdata._wins, reverse=True)
                        for playerdata in malePlayerNamesDatatableTaw11:
                            percent = percentageCal(playerdata._wins,playerdata._losses)
                            print(playerdata._player+" win : %"+str(percent))
                    if taw11mensStatsMenuInput == '7':
                        print("Mens TAW11 Stats")
                        malePlayerNamesDatatableTaw11.sort(key = lambda playerdata: playerdata._wins, reverse=True)
                        for playerdata in malePlayerNamesDatatableTaw11:
                            percent = percentageCal(playerdata._wins,playerdata._losses)
                            print(playerdata._player+" Wins: "+str(playerdata._wins)+" 3-0 wins: "+str(playerdata._win_by_three)+" 3-1 wins: "+str(playerdata._win_by_two)+" 3-2 wins: "+str(playerdata._win_by_one)+" losses: "+str(playerdata._losses)+" win percentage : %"+str(percent))
                if mensOrWomens == 'LADIES':
                    printLadiesStatsoptions()
                    taw11womensStatsMenuInput = input('Enter a number 1-5: ')
                    if taw11womensStatsMenuInput == '1':
                        print("Ladies TAW11 Win Stats")
                        femalePlayerNamesDatatableTaw11.sort(key = lambda playerdata: playerdata._wins, reverse=True)
                        for playerdata in femalePlayerNamesDatatableTaw11:
                            print(playerdata._player+ " number of wins: " +str(playerdata._wins) )
                    if taw11womensStatsMenuInput == '2':
                        print("Ladies TAW11 2-0 Stats")
                        femalePlayerNamesDatatableTaw11.sort(key = lambda playerdata: playerdata._win_by_three, reverse=True)
                        for playerdata in femalePlayerNamesDatatableTaw11:
                            print(playerdata._player+ " number of 2-0 wins: " +str(playerdata._win_by_three))
                    if taw11womensStatsMenuInput == '3':
                        print("Ladies TAW11 2-1 Stats")
                        femalePlayerNamesDatatableTaw11.sort(key = lambda playerdata: playerdata._win_by_one, reverse=True)
                        for playerdata in femalePlayerNamesDatatableTaw11:
                            print(playerdata._player+ " number of 2-1 wins: " +str(playerdata._win_by_one))
                    if taw11womensStatsMenuInput == '4':
                        print("Ladies TAW11 losses Stats")
                        femalePlayerNamesDatatableTaw11.sort(key = lambda playerdata: playerdata._losses, reverse=True)
                        for playerdata in femalePlayerNamesDatatableTaw11:
                            print(playerdata._player+ " number of losses: " +str(playerdata._losses))
                    if taw11womensStatsMenuInput == '5':
                        print("Ladies TAW11 percenatge Stats")
                        femalePlayerNamesDatatableTaw11.sort(key = lambda playerdata: playerdata._wins, reverse=True)
                        for playerdata in femalePlayerNamesDatatableTaw11:
                            percent = percentageCal(playerdata._wins,playerdata._losses)
                            print(playerdata._player+" win : %"+str(percent))
                    if taw11womensStatsMenuInput == '6':
                        print("Ladies TAW11 Stats")
                        femalePlayerNamesDatatableTaw11.sort(key = lambda playerdata: playerdata._wins, reverse=True)
                        for playerdata in femalePlayerNamesDatatableTaw11:
                            percent = percentageCal(playerdata._wins,playerdata._losses)
                            print(playerdata._player+" Wins: "+str(playerdata._wins)+" 2-0 wins: "+str(playerdata._win_by_three)+" 2-1 wins: "+str(playerdata._win_by_one)+" losses: "+str(playerdata._losses)+" win percentage: %"+str(percent))
            elif tournament == 'TBS2':
                if mensOrWomens == 'MEN':
                    printMensStatsoptions()
                    tbs2mensStatsMenuInput = input('Enter a number 1-5: ')
                    if tbs2mensStatsMenuInput == '1':
                        print("Mens TBS2 Win Stats")
                        malePlayerNamesDatatableTbs2.sort(key = lambda playerdata: playerdata._wins, reverse=True)
                        for playerdata in malePlayerNamesDatatableTbs2:
                            print(playerdata._player+ " number of wins: " +str(playerdata._wins) )
                    if tbs2mensStatsMenuInput == '2':
                        print("Mens TBS2 3-0 Stats")
                        malePlayerNamesDatatableTbs2.sort(key = lambda playerdata: playerdata._win_by_three, reverse=True)
                        for playerdata in malePlayerNamesDatatableTbs2:
                            print(playerdata._player+ " number of 3-0 wins: " +str(playerdata._win_by_three))
                    if tbs2mensStatsMenuInput == '3':
                        print("Mens TBS2 3-1 Stats")
                        malePlayerNamesDatatableTbs2.sort(key = lambda playerdata: playerdata._win_by_two, reverse=True)
                        for playerdata in malePlayerNamesDatatableTbs2:
                            print(playerdata._player+ " number of 3-1 wins: " +str(playerdata._win_by_two))
                    if tbs2mensStatsMenuInput == '4':
                        print("Mens TBS2 3-2 Stats")
                        malePlayerNamesDatatableTbs2.sort(key = lambda playerdata: playerdata._win_by_one, reverse=True)
                        for playerdata in malePlayerNamesDatatableTbs2:
                            print(playerdata._player+ " number of 3-2 wins: " +str(playerdata._win_by_one))
                    if tbs2mensStatsMenuInput == '5':
                        print("Mens TBS2 losses Stats")
                        malePlayerNamesDatatableTbs2.sort(key = lambda playerdata: playerdata._losses, reverse=True)
                        for playerdata in malePlayerNamesDatatableTbs2:
                            print(playerdata._player+ " number of losses: " +str(playerdata._losses))
                    if tbs2mensStatsMenuInput == '6':
                        print("Mens TBS2 percenatge Stats")
                        malePlayerNamesDatatableTbs2.sort(key = lambda playerdata: playerdata._wins, reverse=True)
                        for playerdata in malePlayerNamesDatatableTbs2:
                            percent = percentageCal(playerdata._wins,playerdata._losses)
                            print(playerdata._player+" win : %"+str(percent))
                    if tbs2mensStatsMenuInput == '7':
                        print("Mens TBS2 Stats")
                        malePlayerNamesDatatableTbs2.sort(key = lambda playerdata: playerdata._wins, reverse=True)
                        for playerdata in malePlayerNamesDatatableTbs2:
                            percent = percentageCal(playerdata._wins,playerdata._losses)
                            print(playerdata._player+" Wins: "+str(playerdata._wins)+" 3-0 wins: "+str(playerdata._win_by_three)+" 3-1 wins: "+str(playerdata._win_by_two)+" 3-2 wins: "+str(playerdata._win_by_one)+" losses: "+str(playerdata._losses)+" win percentage : %"+str(percent))
                if mensOrWomens == 'LADIES':
                    printLadiesStatsoptions()
                    tbs2womensStatsMenuInput = input('Enter a number 1-5: ')
                    if tbs2womensStatsMenuInput == '1':
                        print("Ladies TBS2 Win Stats")
                        femalePlayerNamesDatatableTbs2.sort(key = lambda playerdata: playerdata._wins, reverse=True)
                        for playerdata in femalePlayerNamesDatatableTbs2:
                            print(playerdata._player+ " number of wins: " +str(playerdata._wins) )
                    if tbs2womensStatsMenuInput == '2':
                        print("Ladies TBS2 2-0 Stats")
                        femalePlayerNamesDatatableTbs2.sort(key = lambda playerdata: playerdata._win_by_three, reverse=True)
                        for playerdata in femalePlayerNamesDatatableTbs2:
                            print(playerdata._player+ " number of 2-0 wins: " +str(playerdata._win_by_three))
                    if tbs2womensStatsMenuInput == '3':
                        print("Ladies TBS2 2-1 Stats")
                        femalePlayerNamesDatatableTbs2.sort(key = lambda playerdata: playerdata._win_by_one, reverse=True)
                        for playerdata in femalePlayerNamesDatatableTbs2:
                            print(playerdata._player+ " number of 2-1 wins: " +str(playerdata._win_by_one))
                    if tbs2womensStatsMenuInput == '4':
                        print("Ladies TBS2 losses Stats")
                        femalePlayerNamesDatatableTbs2.sort(key = lambda playerdata: playerdata._losses, reverse=True)
                        for playerdata in femalePlayerNamesDatatableTbs2:
                            print(playerdata._player+ " number of losses: " +str(playerdata._losses))
                    if tbs2womensStatsMenuInput == '5':
                        print("Ladies TAW11 percenatge Stats")
                        femalePlayerNamesDatatableTbs2.sort(key = lambda playerdata: playerdata._wins, reverse=True)
                        for playerdata in femalePlayerNamesDatatableTbs2:
                            percent = percentageCal(playerdata._wins,playerdata._losses)
                            print(playerdata._player+" win : %"+str(percent))
                    if tbs2womensStatsMenuInput == '6':
                        print("Ladies TBS2 Stats")
                        femalePlayerNamesDatatableTbs2.sort(key = lambda playerdata: playerdata._wins, reverse=True)
                        for playerdata in femalePlayerNamesDatatableTbs2:
                            percent = percentageCal(playerdata._wins,playerdata._losses)
                            print(playerdata._player+" Wins: "+str(playerdata._wins)+" 2-0 wins: "+str(playerdata._win_by_three)+" 2-1 wins: "+str(playerdata._win_by_one)+" losses: "+str(playerdata._losses)+" win percentage: %"+str(percent))
            elif tournament == 'ALL':
                if mensOrWomens == 'MEN':
                    printMensStatsoptions()
                    allmensStatsMenuInput = input('Enter a number 1-7: ')
                    if allmensStatsMenuInput == '1':
                        print("Mens ALL Win Stats")
                        malePlayerNamesDatatableAll.sort(key = lambda playerdata: playerdata._wins, reverse=True)
                        for playerdata in malePlayerNamesDatatableAll:
                            print(playerdata._player+ " number of wins: " +str(playerdata._wins) )
                    if allmensStatsMenuInput == '2':
                        print("Mens ALL Win by 3 Stats")
                        malePlayerNamesDatatableAll.sort(key = lambda playerdata: playerdata._win_by_three, reverse=True)
                        for playerdata in malePlayerNamesDatatableAll:
                            print(playerdata._player+ " number of 3-0 wins: " +str(playerdata._win_by_three))
                    if allmensStatsMenuInput == '3':
                        print("Mens ALL Win by 2 Sets Stats")
                        malePlayerNamesDatatableAll.sort(key = lambda playerdata: playerdata._win_by_two, reverse=True)
                        for playerdata in malePlayerNamesDatatableAll:
                            print(playerdata._player+ " number of 3-1 wins: " +str(playerdata._win_by_two))
                    if allmensStatsMenuInput == '4':
                        print("Mens ALL Win by 1 Set Stats")
                        malePlayerNamesDatatableAll.sort(key = lambda playerdata: playerdata._win_by_one, reverse=True)
                        for playerdata in malePlayerNamesDatatableAll:
                            print(playerdata._player+ " number of 3-2 wins: " +str(playerdata._win_by_one))
                    if allmensStatsMenuInput == '5':
                        print("Mens ALL losses Stats")
                        malePlayerNamesDatatableAll.sort(key = lambda playerdata: playerdata._losses, reverse=True)
                        for playerdata in malePlayerNamesDatatableAll:
                            print(playerdata._player+ " number of losses: " +str(playerdata._losses))
                    if allmensStatsMenuInput == '6':
                        print("Mens ALL percenatge Stats")
                        malePlayerNamesDatatableAll.sort(key = lambda playerdata: playerdata._wins, reverse=True)
                        for playerdata in malePlayerNamesDatatableAll:
                            percent = percentageCal(playerdata._wins,playerdata._losses)
                            print(playerdata._player+" win : %"+str(percent))
                    if allmensStatsMenuInput == '7':
                        print("Mens ALL Stats")
                        malePlayerNamesDatatableAll.sort(key = lambda playerdata: playerdata._wins, reverse=True)
                        for playerdata in malePlayerNamesDatatableAll:
                            percent = percentageCal(playerdata._wins,playerdata._losses)
                            print(playerdata._player+" Wins: "+str(playerdata._wins)+" 3-0 wins: "+str(playerdata._win_by_three)+" 3-1 wins: "+str(playerdata._win_by_two)+" 3-2 wins: "+str(playerdata._win_by_one)+" losses: "+str(playerdata._losses)+" win percentage : %"+str(percent))
                if mensOrWomens == 'LADIES':
                    printLadiesStatsoptions()
                    allwomensStatsMenuInput = input('Enter a number 1-6: ')
                    if allwomensStatsMenuInput == '1':
                        print("Ladies All Win Stats")
                        femalePlayerNamesDatatableAll.sort(key = lambda playerdata: playerdata._wins, reverse=True)
                        for playerdata in femalePlayerNamesDatatableAll:
                            print(playerdata._player+ " number of wins: " +str(playerdata._wins))
                    if allwomensStatsMenuInput == '2':
                        print("Ladies All 2-0 Stats")
                        femalePlayerNamesDatatableAll.sort(key = lambda playerdata: playerdata._win_by_three, reverse=True)
                        for playerdata in femalePlayerNamesDatatableAll:
                            print(playerdata._player+ " number of 2-0 wins: " +str(playerdata._win_by_three))
                    if allwomensStatsMenuInput == '3':
                        print("Ladies All 2-1 Stats")
                        femalePlayerNamesDatatableAll.sort(key = lambda playerdata: playerdata._win_by_one, reverse=True)
                        for playerdata in femalePlayerNamesDatatableAll:
                            print(playerdata._player+ " number of 2-1 wins: " +str(playerdata._win_by_one))
                    if allwomensStatsMenuInput == '4':
                        print("Ladies All losses Stats")
                        femalePlayerNamesDatatableAll.sort(key = lambda playerdata: playerdata._losses, reverse=True)
                        for playerdata in femalePlayerNamesDatatableAll:
                            print(playerdata._player+ " number of losses: " +str(playerdata._losses))
                    if allwomensStatsMenuInput == '5':
                        print("Ladies All percenatge Stats")
                        femalePlayerNamesDatatableAll.sort(key = lambda playerdata: playerdata._wins, reverse=True)
                        for playerdata in femalePlayerNamesDatatableAll:
                            percent = percentageCal(playerdata._wins,playerdata._losses)
                            print(playerdata._player+" win : %"+str(percent))
                    if allwomensStatsMenuInput == '6':
                        print("Ladies All Stats")
                        femalePlayerNamesDatatableAll.sort(key = lambda playerdata: playerdata._wins, reverse=True)
                        for playerdata in femalePlayerNamesDatatableAll:
                            percent = percentageCal(playerdata._wins,playerdata._losses)
                            print(playerdata._player+" Wins: "+str(playerdata._wins)+" 2-0 wins: "+str(playerdata._win_by_three)+" 2-1 wins: "+str(playerdata._win_by_one)+" losses: "+str(playerdata._losses)+" win percentage: %"+str(percent))
# calculates the % of wins
def percentageCal(playerWins, playerlosses):
    if (playerWins + playerlosses) == 0:
        percentageOfWins = 0
    else:
        percentageOfWins = (playerWins / (playerWins + playerlosses)) * 100
        percentageOfWins = round(percentageOfWins,2)
    return percentageOfWins
# menu
def printMensStatsoptions():
    print("1: View mens win stats\n")
    print("2: View mens 3-0 win stats\n")
    print("3: view mens 3-1 win stats\n")
    print("4: view mens 3-2 win stats\n")
    print("5: view mens loss stats\n")
    print("6: view mens win percentage stats\n")
    print("7: Totals for tournament\n")
# menu
def printLadiesStatsoptions():
    print("1: View ladies win stats\n")
    print("2: View ladies 2-0 win stats\n")
    print("3: view ladies 2-1 win stats\n")
    print("4: view ladies loss stats\n")
    print("5: view ladies win percentage stats\n")
    print("6: Totals for tournament")
printdata()
malePlayers()
femalePlayers()
menu()
