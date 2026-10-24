import random

options = ["rock", "paper", "scissors"]

gameStatus = True

computerScore = 0
playerScore = 0

while gameStatus == True:
    
    computerChoice = random.choice(options)

    userChoice = input("rock, paper, scissors? (type 'stop' to end game) ").lower()

    if userChoice in options:
    
        print("Computer Choice: " + computerChoice)
    
        if userChoice == "rock":
            if computerChoice == "rock":
                print("tie")
            elif computerChoice == "paper":
                print("computer wins")
                computerScore = computerScore + 1
            elif computerChoice == "scissors":
                print("you win")
                playerScore = playerScore + 1
        
        elif userChoice == "paper":
            if computerChoice == "rock":
                print("you win")
                playerScore = playerScore + 1
            elif computerChoice == "paper":
                print("tie")
            elif computerChoice == "scissors":
                print("computer wins")
                computerScore = computerScore + 1
        
        elif userChoice == "scissors":
            if computerChoice == "rock":
                print("computer wins")
                computerScore = computerScore + 1
            elif computerChoice == "paper":
                print("you win")
                playerScore = playerScore + 1
            elif computerChoice == "scissors":
                print("tie")

    elif userChoice == "stop".lower():
        print("You are quitting the game.")
        print("here is the final score: ")
        print("Computer score: " + str(computerScore))
        print("Player score: " + str(playerScore))
        if computerScore > playerScore:
            print("computer wins overall")
        elif playerScore > computerScore:
            print("you win overall")
        else:
            print("tie")
        break
    
    else:
        print("oop typo?")
