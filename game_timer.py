import time
import matplotlib.pyplot as plt

#returns max number in a list
def maxi(list):
    max = 0
    for time in list:
        if time > max:
            max = time
    return max

#returns sum of numbers in a list
def sumi(list):
    sum = 0
    for time in list:
        sum = sum + time
    return sum

#returns average given a sum and the number of items
def avgi(sum, leng):
    avg = sum/leng
    return avg


listForPlayers = {}
playerList = []
num = 0

#ask user for a list of players
while True:
    nam = input("Input the name of a player. Write 'done' when finished: ")
    if nam == "":
        continue
    if nam == "done":
        break
    playerList.append(nam)
    num = num+1

print("The players are:")
for player in playerList:
    print(player)
    listForPlayers[player] = ()

#ask user to indicate when the game starts
while True:
  inp = input("Type 'start' when ready to begin timing: ")
  inp = inp.lower()
  if inp == "start" or inp == "Start":
    break
  else:
    continue

#game starts; start tracking user's length of turn
numPlayers = len(playerList)
turnOverall = 0
print("NOTE: Type 'end' to end game. Type 'next' to move to the next player without recording a time.")
while True:
    #determine which player's turn it is
    modulo = turnOverall % numPlayers
    playerName = playerList[modulo]
    timeA = time.perf_counter()
    inp = input("Press ENTER when " + playerName + "'s turn is over.  ")
    if inp.lower() == "end":
        break
    if inp.lower() == "next":
        turnOverall = turnOverall + 1
        continue

    timeB = time.perf_counter()
    timeTurn = timeB-timeA
    timeTurn = round(timeTurn,0)
    turnOverall = turnOverall + 1
    listPlayer = list(listForPlayers[playerName])
    listPlayer.append(timeTurn)
    listForPlayers[playerName] = tuple(listPlayer)

#run metrics on player's turn time numbers
maxList = []
avgList = []
for playerName in playerList:
    max = maxi(listForPlayers[playerName])
    maxList.append(max)
    sum = sumi(listForPlayers[playerName])
    leng = len(listForPlayers[playerName])
    avg = avgi(sum, leng)
    avgList.append(avg)

plt.bar(playerList,maxList)
plt.xlabel("Players")
plt.ylabel("Max turn length (seconds)")
plt.show()

plt.bar(playerList,avgList)
plt.xlabel("Players")
plt.ylabel("Average turn length (seconds)")
plt.show()
