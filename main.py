import random
import time

slash = "---------------"

over = 1
brain = 0

print("Tic Tac Toe!!!")
print("")

table = [["-", "-", "-"],
         ["-", "-", "-"],
         ["-", "-", "-"]]


def gameEnd():
    global over

    if table[0][0] == "X" and table[0][1] == "X" and table[0][2] == "X":
        over = 60
    if table[1][0] == "X" and table[1][1] == "X" and table[1][2] == "X":
        over = 60
    if table[2][0] == "X" and table[2][1] == "X" and table[2][2] == "X":
        over = 60

    if table[0][0] == "X" and table[1][0] == "X" and table[2][0] == "X":
        over = 60
    if table[0][1] == "X" and table[1][1] == "X" and table[2][1] == "X":
        over = 60
    if table[0][2] == "X" and table[1][2] == "X" and table[2][2] == "X":
        over = 60

    if table[0][0] == "O" and table[0][1] == "O" and table[0][2] == "O":
        over = 50
    if table[1][0] == "O" and table[1][1] == "O" and table[1][2] == "O":
        over = 50
    if table[2][0] == "O" and table[2][1] == "O" and table[2][2] == "O":
        over = 50

    if table[0][0] == "O" and table[1][0] == "O" and table[2][0] == "O":
        over = 50
    if table[0][1] == "O" and table[1][1] == "O" and table[2][1] == "O":
        over = 50
    if table[0][2] == "O" and table[1][2] == "O" and table[2][2] == "O":
        over = 50

    if table[0][0] == "X" and table[1][1] == "X" and table[2][2] == "X":
        over = 60
    if table[0][2] == "X" and table[1][1] == "X" and table[2][0] == "X":
        over = 60

    if table[0][0] == "O" and table[1][1] == "O" and table[2][2] == "O":
        over = 50
    if table[0][2] == "O" and table[1][1] == "O" and table[0][2] == "O":
        over = 50

    return over


def blank():
    runr = 0
    runp = 0

    blankSpace = 0

    while runr < 3:
        while runp < 3:
            if table[runr][runp] == "-":
                blankSpace += 1
            runp += 1
        runr += 1
        runp = 0
    return blankSpace


def present():
    print(slash)
    print(table[0])

    print(table[1])

    print(table[2])
    print(slash)
    print("")


def userTurn():
    global ypos, xpos
    try:
        xpos = int(input("enter the row u want to mark X:"))
        ypos = int(input("enter the column u want to mark X:"))
    except ValueError:
        print("invalid input!")
        userTurn()
        return None

    inval = 0

    if xpos <= 0:
        inval = 1

    if xpos >= 4:
        inval = 1

    if ypos >= 4:
        inval = 1

    if ypos <= 0:
        inval = 1

    if inval == 0:
        if table[ypos - 1][xpos - 1] == "-":
            table[ypos - 1][xpos - 1] = "X"
        else:
            print("")
            print("the position has already been marked please try again:")
            print("")
            userTurn()
    if inval == 1:
        print("")
        print("invalid position please try again")
        print("")
        userTurn()


def compMove():
    xpos = random.randrange(0, 3, 1)
    ypos = random.randrange(0, 3, 1)

    if table[xpos][ypos] == "-":
        table[xpos][ypos] = "O"
        print("")
        print("Computers Turn:")
    else:
        compMove()


def compMoveBrain():
    global brain
    if table[0][0] == "-" and table[0][1] == "O" and table[0][2] == "O":
        table[0][0] = "O"
    elif table[0][0] == "O" and table[0][1] == "-" and table[0][2] == "O":
        table[0][1] = "O"
    elif table[0][0] == "O" and table[0][1] == "O" and table[0][2] == "-":
        table[0][2] = "O"



    elif table[1][0] == "-" and table[1][1] == "O" and table[1][2] == "O":
        table[1][0] = "O"
    elif table[1][0] == "O" and table[1][1] == "-" and table[1][2] == "O":
        table[1][1] = "O"
    elif table[1][0] == "O" and table[1][1] == "O" and table[1][2] == "-":
        table[1][2] = "O"



    elif table[2][0] == "-" and table[2][1] == "O" and table[2][2] == "O":
        table[2][0] = "O"
    elif table[2][0] == "O" and table[2][1] == "-" and table[2][2] == "O":
        table[2][1] = "O"
    elif table[2][0] == "O" and table[2][1] == "O" and table[2][2] == "-":
        table[2][2] = "O"



    elif table[0][0] == "-" and table[1][0] == "O" and table[2][0] == "O":
        table[0][0] = "O"
    elif table[0][0] == "O" and table[1][0] == "-" and table[2][0] == "O":
        table[1][0] = "O"
    elif table[0][0] == "O" and table[1][0] == "O" and table[2][0] == "-":
        table[2][0] = "O"



    elif table[0][1] == "-" and table[1][1] == "O" and table[2][1] == "O":
        table[0][1] = "O"
    elif table[0][1] == "O" and table[1][1] == "-" and table[2][1] == "O":
        table[1][1] = "O"
    elif table[0][1] == "O" and table[1][1] == "O" and table[2][1] == "-":
        table[2][1] = "O"


    elif table[0][2] == "-" and table[1][2] == "O" and table[2][2] == "O":
        table[0][2] = "O"
    elif table[0][2] == "O" and table[1][2] == "-" and table[2][2] == "O":
        table[1][2] = "O"
    elif table[0][2] == "O" and table[1][2] == "O" and table[2][2] == "-":
        table[2][2] = "O"





    elif table[0][0] == "-" and table[0][1] == "X" and table[0][2] == "X":
        table[0][0] = "O"
        brain = 1
    elif table[0][0] == "X" and table[0][1] == "-" and table[0][2] == "X":
        table[0][1] = "O"
        brain = 1
    elif table[0][0] == "X" and table[0][1] == "X" and table[0][2] == "-":
        table[0][2] = "O"
        brain = 1



    elif table[1][0] == "-" and table[1][1] == "X" and table[1][2] == "X":
        table[1][0] = "O"
        brain = 1
    elif table[1][0] == "X" and table[1][1] == "-" and table[1][2] == "X":
        table[1][1] = "O"
        brain = 1
    elif table[1][0] == "X" and table[1][1] == "X" and table[1][2] == "-":
        table[1][2] = "O"
        brain = 1



    elif table[2][0] == "-" and table[2][1] == "X" and table[2][2] == "X":
        table[2][0] = "O"
        brain = 1
    elif table[2][0] == "X" and table[2][1] == "-" and table[2][2] == "X":
        table[2][1] = "O"
        brain = 1
    elif table[2][0] == "X" and table[2][1] == "X" and table[2][2] == "-":
        table[2][2] = "O"
        brain = 1



    elif table[0][0] == "-" and table[1][0] == "X" and table[2][0] == "X":
        table[0][0] = "O"
        brain = 1
    elif table[0][0] == "X" and table[1][0] == "-" and table[2][0] == "X":
        table[1][0] = "O"
        brain = 1
    elif table[0][0] == "X" and table[1][0] == "X" and table[2][0] == "-":
        table[2][0] = "O"
        brain = 1



    elif table[0][1] == "-" and table[1][1] == "X" and table[2][1] == "X":
        table[0][1] = "O"
        brain = 1
    elif table[0][1] == "X" and table[1][1] == "-" and table[2][1] == "X":
        table[1][1] = "O"
        brain = 1
    elif table[0][1] == "X" and table[1][1] == "X" and table[2][1] == "-":
        table[2][1] = "O"
        brain = 1



    elif table[0][2] == "-" and table[1][2] == "X" and table[2][2] == "X":
        table[0][2] = "O"
        brain = 1
    elif table[0][2] == "X" and table[1][2] == "-" and table[2][2] == "X":
        table[1][2] = "O"
        brain = 1
    elif table[0][2] == "X" and table[1][2] == "X" and table[2][2] == "-":
        table[2][2] = "O"
        brain = 1



    elif table[0][0] == "-" and table[1][1] == "X" and table[2][2] == "X":
        table[0][0] = "O"
        brain = 1
    elif table[0][0] == "X" and table[1][1] == "-" and table[2][2] == "X":
        table[1][1] = "O"
        brain = 1
    elif table[0][0] == "X" and table[1][1] == "X" and table[2][2] == "-":
        table[2][2] = "O"
        brain = 1



    elif table[0][2] == "-" and table[1][1] == "X" and table[2][0] == "X":
        table[0][2] = "O"
        brain = 1
    elif table[0][2] == "X" and table[1][1] == "-" and table[2][0] == "X":
        table[1][1] = "O"
        brain = 1
    elif table[0][2] == "X" and table[1][1] == "X" and table[2][0] == "-":
        table[2][0] = "O"
        brain = 1
    else:
        brain = 0
    return brain


def FM():
    global firstMove
    try:
        firstMove = int(input("would you like to go first? if yes type \"1\" else enter any other value: "))
        present()
    except ValueError:
        print("invalid input!")
        FM()


FM()

if firstMove == 1:
    while blank() != 0:
        over = gameEnd()
        if blank() != 0:
            userTurn()
            present()
            gameEnd()
        if blank() != 0:
            gg = compMoveBrain()
            if gg == 0:
                compMove()
            present()
            gameEnd()
        if over == 60:
            print("The User Wins!")
            quit()
        if over == 50:
            print("The Computer Wins!")
            quit()
    print("")
    print("Game Over")
    if over == 1:
        print("No One Wins...")


else:
    while blank() != 0:
        over = gameEnd()

        if blank() != 0:
            gg = compMoveBrain()
            if gg == 0:
                compMove()
            present()
            gameEnd()

        if blank() != 0:
            userTurn()
            present()
            gameEnd()
        if over == 60:
            print("The User Wins!")
            quit()
        if over == 50:
            print("The Computer Wins!")
            quit()
    print("")
    print("Game Over")
    if over == 1:
        print("No One Wins...")

time.sleep(5)
