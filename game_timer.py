import time
##import matplotlib
##import matplotlib.pyplot as playerList
##import numpy as np

def maxi(list):
    max = 0
    for time in list:
        if time > max:
            max = time
    return max

def sumi(list):
    sum = 0
    for time in list:
        sum = sum + time
    return sum

def avgi(sum, leng):
    avg = sum/leng
    return avg


listForPlayers = {}
playerList = []
num = 0
while True:
    nam = input("Input the name of a player. Write done when finished: ")
    if nam == "done":
        break
    playerList.append(nam)
    num = num+1

print("The players are:")
for player in playerList:
    print(player)
    listForPlayers[player] = ()


while True:
  inp = input("Type start when ready to begin timing: ")
  inp = inp.lower()
  if inp == "start" or inp == "Start":
    break
  else:
    continue

numPlayers = len(playerList)
turnOverall = 0
print(turnOverall)
while True:
    #determine which player's turn it is
    modulo = turnOverall % numPlayers
    print(turnOverall)
    playerName = playerList[modulo]
    timeA = time.perf_counter()
    inp = input("Press ENTER when " + playerName + "'s turn is over. Type 'end' to end game. Type 'next' to move to the next player without recording a time.  ")
    if inp.lower() == "end":
        break
    if inp.lower() == "next":
        turnOverall = turnOverall + 1
        continue

    timeB = time.perf_counter()
    timeTurn = timeB-timeA
    timeTurn = round(timeTurn,0)
    print(timeTurn)
    turnOverall = turnOverall + 1
    listPlayer = list(listForPlayers[playerName])
    listPlayer.append(timeTurn)
    listForPlayers[playerName] = tuple(listPlayer)

maxList = []
avgList = []
for playerName in playerList:
    #print(playerName)
    #print(listForPlayers[playerName])

    max = maxi(listForPlayers[playerName])
    maxList.append(max)

    sum = sumi(listForPlayers[playerName])
    leng = len(listForPlayers[playerName])
    avg = avgi(sum, leng)
    avgList.append(avg)
    ##num_entries = num_entries(listForPlayers[playerName])
    ##maxList.append(max)
print(playerList)
print(maxList)
print(avgList)
