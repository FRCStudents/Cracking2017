import random

rooms = [{'id': 1, 'width': 5, 'height': 7, 'doors':[{'side': 'e', 'fromCorner': 2},{'side': 's', 'fromCorner': 2}],'posX':0, 'posY':0, 'personX':0, 'personY':0},
	     {'id': 2, 'width': 5, 'height': 7, 'doors':[{'side': 'w', 'fromCorner': 2},{'side': 's', 'fromCorner': 3}], 'posX':0, 'posY':0, 'personX':0, 'personY':0},
	     {'id': 3, 'width': 5, 'height': 7, 'doors':[{'side': 'n', 'fromCorner': 2},{'side': 'e', 'fromCorner': 2}], 'posX':0, 'posY':0, 'personX':0, 'personY':0},
	     {'id': 4, 'width': 5, 'height': 7, 'doors':[{'side': 'n', 'fromCorner': 3},{'side': 'w', 'fromCorner': 2}], 'posX':0, 'posY':0, 'personX':0, 'personY':0}]

playerPosition = {'posX':0, 'posY':0, 'room': 1}
treasurePosition = {'posX':0, 'posY':0, 'room': 1}

def initializeGame():
	playerPosition['posX'] = random.randint(1, 5)
	playerPosition['posY'] = random.randint(1, 2)
	playerPosition['room'] = random.randint(1, 4)

	treasurePosition['posX'] = random.randint(1, 5)
	treasurePosition['posY'] = random.randint(1, 2)
	treasurePosition['room'] = random.randint(1, 4)

def getRoom(room):
    return rooms[room - 1]

def displayBoard():
    print("North")
    print("|-----| |-------|")
    print("|1    | |2      |")
    print("|               |")
    print("|-  --| |--  ---|")
    print("|3    | |4      |")
    print("|               |")
    print("|-----| |-------|")

def displayPosition():
	print("Player: (r/x/y) " + str(playerPosition['room']) + str(playerPosition['posX']) + str(playerPosition['posY']))

def displayDoor(doors):
    for door in doors:
        print("\tDoor: " + door['side'] + "//" + str(door['fromCorner']))

def displayRoom(room):
    for x in room.keys():
            if x == 'doors':
                displayDoor(room[x])
            else:
                print(x + ":" + str(room[x]))

def displayRooms():
    for room in rooms:
        displayRoom(room)

def setPlayer(x, y, room):
    playerPosition['room'] = room
    playerPosition['posX'] = x
    playerPosition['posY'] = y

def positionInNextRoom(direction):
    if playerPosition['room'] == 1 and direction == 'e':
        setPlayer(1,2,2)
    if playerPosition['room'] == 1 and direction == 's':
        setPlayer(2,1,3)

    if playerPosition['room'] == 2 and direction == 'w':
        setPlayer(5,2,1)
    if playerPosition['room'] == 2 and direction == 's':
        setPlayer(3,1,4)

    if playerPosition['room'] == 3 and direction == 'e':
        setPlayer(1,2,4)
    if playerPosition['room'] == 3 and direction == 'n':
        setPlayer(2,2,1)

    if playerPosition['room'] == 4 and direction == 'w':
        setPlayer(2,5,3)
    if playerPosition['room'] == 4 and direction == 'n':
        setPlayer(3,2,2)

def goEast():
    if playerPosition['posX'] > 4:
        if playerPosition['posY'] == 2 and (playerPosition['room'] == 1 or playerPosition['room'] == 3):
            print("You went into the next room")
            positionInNextRoom('e')
        else:
            print("You bumped into the wall")
    else:
        playerPosition['posX'] += 1

def goWest():
    if playerPosition['posX'] < 2:
        if playerPosition['posY'] == 2 and (playerPosition['room'] == 3 or playerPosition['room'] == 4):
            print("You went into the next room")
            positionInNextRoom('w')
        else:
            print("You bumped into the wall")
    else:
        playerPosition['posX'] -= 1

def goSouth():
    if playerPosition['posY'] > 1:
        if (playerPosition['posX'] == 2 and playerPosition['room'] == 1) or (playerPosition['posX'] == 3 and playerPosition['room'] == 2):
            print("You went into the next room")
            positionInNextRoom('s')
        else:
            print("You bumped into the wall")
    else:
        playerPosition['posY'] += 1

def goNorth():
    if playerPosition['posY'] < 2:
        if (playerPosition['posX'] == 2 and playerPosition['room'] == 3) or (playerPosition['posX'] == 3 and playerPosition['room'] == 4):
            print("You went into the next room")
            positionInNextRoom('n')
        else:
            print("You bumped into the wall")
    else:
        playerPosition['posY'] -= 1


def getResponse():
    response = input()
    if(response == 'w'):
        goWest()
    if(response == 'e'):
        goEast()
    if(response == 'n'):
        goNorth()
    if(response == 's'):
        goSouth()

def adventure():
    print("You are in the NorthWest corner of the house")
    while not findTreasure():
        print("Where do you go? ")
        getResponse()

def findTreasure():
	if playerPosition['posX'] == treasurePosition['posX'] and playerPosition['posY'] == treasurePosition['posY'] and playerPosition['room'] == treasurePosition['room']:
		print("You have just found the ruddy treasure! Go Dude!")
		return True
	else:
		#displayPosition()
		return False

initializeGame()
#displayBoard()
#displayRooms()
adventure()
