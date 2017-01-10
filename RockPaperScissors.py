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


    #while the user doesn't choose a valid choice from the menu the program loops to ask for a valid input
    while (playerChoice != 'r' and playerChoice != 'p' and playerChoice != 's' and playerChoice != 'q'):
        print("Enter a valid input")
        playerChoice = input("")

    #if the user inputs q the program exits the main loop to stop after printing the final score
    if (playerChoice == 'q'):
        print("Final Score:")
        print("Computer: " + str(computerScore))
        print("You: " + str(playerScore))

    #if the player's choice of r,p,s = RPS[1:r, 2:p, 3:p] then both players get a point and Tie! is displayed
    elif(str(playerChoice) == RPS[str(computerChoice)]):
        computerScore += 1
        playerScore += 1
        print("Computer chose " + RPS[str(computerChoice)])
        print("Tie!")

    #if  the player's choice of RPS[r:3, p:1, s:2] = the computer's choice of 3, 1, or 2 then the player is awarded a point and You win! is displayed
    elif(RPS[playerChoice] == str(computerChoice)):
        playerScore += 1
        print("Computer chose " + RPS[str(computerChoice)])
        print("You win!")

    #any other results will be the computer's choice beating the player's choice and computer will be awarded a point and You lose! is displayed
    else:
        computerScore += 1
        print("Computer chose " + RPS[str(computerChoice)])
        print("You lose!")
