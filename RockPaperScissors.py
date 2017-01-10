from random import randrange

RPS = {}

RPS['r'] = '3'
RPS['p'] = '1'
RPS['s'] = '2'
RPS['1'] = 'r'
RPS['2'] = 'p'
RPS['3'] = 's'

computerScore = 0
playerScore = 0
playerChoice = ''

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
    playerChoice = input("")


    while (playerChoice != 'r' and playerChoice != 'p' and playerChoice != 's' and playerChoice != 'q'):
        print("Enter a valid input")
        playerChoice = input("")

    if (playerChoice == 'q'):
        print("Final Score:")
        print("Computer: " + str(computerScore))
        print("You: " + str(playerScore))
        
    elif(str(playerChoice) == RPS[str(computerChoice)]):
        computerScore += 1
        playerScore += 1
        print("Computer chose " + RPS[str(computerChoice)])
        print("Tie!")

    elif(RPS[playerChoice] == str(computerChoice)):
        playerScore += 1
        print("Computer chose " + RPS[str(computerChoice)])
        print("You win!")

    else:
        computerScore += 1
        print("Computer chose " + RPS[str(computerChoice)])
        print("You lose!")
