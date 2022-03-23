# Boolean Based Player change True or False | X or O
# Input -> Check for errors
# Status Check
    # Tied
    # Winner found
# Repeat

from logging import PlaceHolder


player = 'X'

playerChoice = True
playerHolder = ""
count = 0
arena = ["", "", "", "", "", "", "", "", ""]
occupancy = ["", "", "", "", "", "", "", "", ""]

while True:

    if (arena[0] == arena[1]) and (arena[1] == arena[2]) and (arena[0] != "" and arena[1] != "" and arena[2] != ""):
        print(f"{playerHolder} is the Winner")
        break
    elif (arena[3] == arena[4]) and (arena[4] == arena[5]) and (arena[3] != "" and arena[4] != "" and arena[5] != ""):
        print(f"{playerHolder} is the Winner")
        break
    elif (arena[6] == arena[7]) and (arena[7] == arena[8]) and (arena[6] != "" and arena[7] != "" and arena[8] != ""):
        print(f"{playerHolder} is the Winner")
        break 
    elif (arena[0] == arena[4]) and (arena[4] == arena[8]) and (arena[0] != "" and arena[4] != "" and arena[8] != ""):
        print(f"{playerHolder} is the Winner")
        break
    elif (arena[2] == arena[4]) and (arena[4] == arena[6]) and (arena[2] != "" and arena[4] != "" and arena[6] != ""):
        print(f"{playerHolder} is the Winner")
        break
    elif (arena[0] == arena[3]) and (arena[3] == arena[6]) and (arena[0] != "" and arena[3] != "" and arena[6] != ""):
        print(f"{playerHolder} is the Winner")
        break
    elif (arena[1] == arena[4]) and (arena[4] == arena[7]) and (arena[1] != "" and arena[4] != "" and arena[7] != ""):
        print(f"{playerHolder} is the Winner")
        break
    elif (arena[2] == arena[5]) and (arena[5] == arena[8]) and (arena[2] != "" and arena[5] != "" and arena[8] != ""):
        print(f"{playerHolder} is the Winner")
        break

    if playerChoice == True:
        player = 'X'
        playerHolder = "Player 1"
        playerChoice = False
    else:
        playerHolder = "Player 2"
        player ='O'
        playerChoice = True

    userInput = int(input(f"{playerHolder}'s Turn, Choose your position of choice"))

    if arena[userInput] is occupancy[userInput]:
        arena[userInput] = player
        occupancy[userInput] = "Filled"
        count = count + 1

    # for x in range(0,3):
    #     str = "| " + str(arena[x])
    #     print(str)
    
    # for x in range(3,6):
    #     str = "| " + str(arena[x])
    #     print(str)

    # for x in range(6,9):
    #     str = "| " + str(arena[x])
    #     print(str)
    
    print(arena)
    
    if occupancy.count("Filled") == 8:
        print("The Game is tied, None of you won. Try Again!")
        break
    
