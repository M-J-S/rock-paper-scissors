from random import randrange

RPShash = {}

RPShash['1'] = '3'
RPShash['2'] = '1'
RPShash['3'] = '2'

computerScore = 0
playerScore = 0
playerChoice = ''

while playerChoice != 'q':
    #rock, paper, scissors instructions
    print("------------------------------------------------------------------")
    print("rock, paper, scissors!")
    print("\n1 = rock")
    print("2 = paper")
    print("3 = scissors")
    print("q = quit")
    print("------------------------------------------------------------------")

    #computer's random choice (Can be either 1, 2, or 3)
    computerChoice = randrange(1, 4)
    

    #Takes input from player and then lowercases incase player enters a capital letter
    playerChoice = input("")


    while (playerChoice != '1' and playerChoice != '2' and playerChoice != '3' and playerChoice != 'q'):
        print("Enter a valid input")
        playerChoice = input("")

    if (playerChoice == 'q'):
        print("Final Score:")
        print("Computer: " + str(computerScore))
        print("You: " + str(playerScore))
        
    elif(str(playerChoice) == str(computerChoice)):
        computerScore += 1
        playerScore += 1
        print("Computer chose " + str(computerChoice))
        print("Tie!")

    elif(RPShash[playerChoice] == str(computerChoice)):
        playerScore += 1
        print("Computer chose " + str(computerChoice))
        print("You win!")

    elif(RPShash[str(computerChoice)] == playerChoice):
        computerScore += 1
        print("Computer chose " + str(computerChoice))
        print("You lose!")
