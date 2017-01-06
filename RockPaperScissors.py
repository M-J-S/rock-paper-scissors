from random import randrange

#rock, paper, scissors instructions
print("------------------------------------------------------------------")
print("rock, paper, scissors!")
print("\nr = rock")
print("p = paper")
print("s = scissors")
print("q = quit")
print("------------------------------------------------------------------")

#computer's random choice (Can be either 1, 2, or 3)
computerChoice = randrange(1, 4)


#Takes input from player and then lowercases incase player enters a capital letter
playerChoice = input("").lower()

while playerChoice != 'q':

    #converts player's choice to a number to make comparing to the computer's choice easier or tells player their selection isn't valid
    if (playerChoice == 'r'):
        playerNumber = 1
        if (computerChoice == 1):
            print("Computer chose rock")
            print("tie, play again? y/n")
        elif (computerChoice == 2):
            print("Computer chose paper")
            print("you lose, play again? y/n")
        else:
            print("Computer chose scissors")
            print("you win, play again? y/n")
        break
    elif (playerChoice == 'p'):
        playerNumber = 2
        if (computerChoice == 1):
            print("Computer chose rock")
            print("you win, play again? y/n")
        elif (computerChoice == 2):
            print("Computer chose paper")
            print("tie, play again? y/n")
        else:
            print("Computer chose scissors")
            print("you lose, play again? y/n")
        break
    elif (playerChoice == 's'):
        playerNumber = 3
        if (computerChoice == 1):
            print("Computer chose rock")
            print("you lose, play again? y/n")
        elif (computerChoice == 2):
            print("Computer chose paper")
            print("you win, play again? y/n")
        else:
            print("Computer chose scissors")
            print("tie, play again? y/n")
        break
    else:
        print("Enter a valid input")
        playerChoice = input("").lower()




