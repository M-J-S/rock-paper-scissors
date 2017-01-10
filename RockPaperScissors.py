from random import randrange

#global variables to keep track of score
computerScore = 0
playerScore = 0
playerChoice = ''
yesOrNo = ''

while playerChoice != 'q':
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

    while (playerChoice != 'r' and playerChoice != 'p' and playerChoice != 's' and playerChoice != 'q'):
        print("Enter a valid input")
        playerChoice = input("").lower()

    #converts player's choice to a number to make comparing to the computer's choice easier or tells player their selection isn't valid
    #player chooses rock and 3 options for whatever computer chooses
    if (playerChoice == 'r'):
        playerNumber = 1
        if (computerChoice == 1):
            print("Computer chose rock")
            print("tie, score:")
            print("Computer: " + str(computerScore))
            print("You: " + str(playerScore))
        elif (computerChoice == 2):
            print("Computer chose paper")
            computerScore += 1
            print("you lose, score:")
            print("Computer: " + str(computerScore))
            print("You: " + str(playerScore))
        else:
            print("Computer chose scissors")
            playerScore += 1
            print("you win, score:")
            print("Computer: " + str(computerScore))
            print("You: " + str(playerScore))
        print("Play again? y/n")
        yesOrNo = input("").lower()
        
        while (yesOrNo != 'n' and yesOrNo != 'y'):
            print("Enter a valid input")
            yesOrNo = input("").lower()

        if (yesOrNo == 'y'):
            print("new game")
        if (yesOrNo == 'n'):
            playerChoice == 'q'
            break
        
            
    #player chooses paper and 3 options for whatever computer chooses
    elif (playerChoice == 'p'):
        playerNumber = 2
        if (computerChoice == 1):
            print("Computer chose rock")
            playerScore += 1
            print("you win, score:")
            print("Computer: " + str(computerScore))
            print("You: " + str(playerScore))
        elif (computerChoice == 2):
            print("Computer chose paper")
            print("tie, score:")
            print("Computer: " + str(computerScore))
            print("You: " + str(playerScore))
        else:
            print("Computer chose scissors")
            computerScore += 1
            print("you lose, score:")
            print("Computer: " + str(computerScore))
            print("You: " + str(playerScore))
            
        print("Play again? y/n")
        yesOrNo = input("").lower()
        
        while (yesOrNo != 'n' and yesOrNo != 'y'):
            print("Enter a valid input")
            yesOrNo = input("").lower()

        if (yesOrNo == 'y'):
            print("new game")
        if (yesOrNo == 'n'):
            playerChoice == 'q'
            break
        
            
    #player chooses scissors and 3 options for whatever computer chooses
    elif (playerChoice == 's'):
        playerNumber = 3
        if (computerChoice == 1):
            print("Computer chose rock")
            computerScore += 1
            print("you lose, score:")
            print("Computer: " + str(computerScore))
            print("You: " + str(playerScore))
        elif (computerChoice == 2):
            print("Computer chose paper")
            playerScore += 1
            print("you win, score:")
            print("Computer: " + str(computerScore))
            print("You: " + str(playerScore))
        else:
            print("Computer chose scissors")
            print("tie, score:")
            print("Computer: " + str(computerScore))
            print("You: " + str(playerScore))
            
        print("Play again? y/n")
        yesOrNo = input("").lower()
        
        while (yesOrNo != 'n' and yesOrNo != 'y'):
            print("Enter a valid input")
            yesOrNo = input("").lower()

        if (yesOrNo == 'y'):
            print("new game")
        if (yesOrNo == 'n'):
            playerChoice == 'q'
            break
        
    elif (playerChoice == 'q'):
        print("Final Score:")
        print("Computer: " + str(computerScore))
        print("You: " + str(playerScore))





