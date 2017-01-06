from random import randrange

#rock, paper, scissors instructions 
print("rock, paper, scissors!")
print("r = rock")
print("p = paper")
print("s = scissors")
print("q = quit")

#computer's random choice (Can be either 1, 2, or 3)
computerChoice = randrange(1, 4)


#Takes input from player and then lowercases incase player enters a capital letter
playerChoice = input("").lower()

while playerChoice != 'q':

    #converts player's choice to a number to make comparing to the computer's choice easier or tells player their selection isn't valid
    if (playerChoice == 'r'):
        playerNumber = 1
        if (computerChoice == 1):
            print("tie")
        elif (computerChoice == 2):
            print("you lose")
        else:
            print("you win")
        break
    elif (playerChoice == 'p'):
        playerNumber = 2
        if (computerChoice == 1):
            print("you win")
        elif (computerChoice == 2):
            print("tie")
        else:
            print("you lose")
        break
    elif (playerChoice == 's'):
        playerNumber = 3
        if (computerChoice == 1):
            print("you lose")
        elif (computerChoice == 2):
            print("you win")
        else:
            print("tie")
        break
    else:
        print("Enter a valid input")
        playerChoice = input("").lower()




