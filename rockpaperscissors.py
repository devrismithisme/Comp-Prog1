greeting = input("Welcome to rock, paper, scissors. Would you like to play? 'yes' or 'no'?  ")

if greeting in ("yes"):
    Player1 = input("Player1, do you choose 'rock', 'paper', or 'scissors'?  ")
    Player2 = input("Player2, do you choose 'rock', 'paper', or 'scissors'?  ")
    if Player1 == "rock" and Player2 == "rock":
        print("It is a tie.")
    if Player1 == "paper" and Player2 == "paper":
        print("It is a tie.")
    if Player1 == "scissors" and Player2 == "scissors":
        print("It is a tie")
    
    if Player1 == "rock" and Player2 == "paper":
        print("Congratulations Player2, you win!")
    if Player1 == "rock" and Player2 == "scissors":
        print("Congratulations Player1, you win!")
    
    if Player1 == "paper" and Player2 == "rock":
        print("Congratulations Player1, you win!")
    if Player1 == "paper" and Player2 == "scissors":
        ("Congratulations Player2, you win!")
    
    if Player1 == "scissors" and Player2 == "rock":
        print("Congratulations Player2, you win!")
    if Player1 == "scissors" and Player2 == "paper":
        print("Congratulations Player1, you win!")
else:
    print("Why on earth are you here then?!") 
    
greeting2 = input("Would you like to play again? 'yes' or 'no'?  ")

if greeting2 in ("yes"):
    print("Just rerun")
else:
    print("Goodbye then") 
