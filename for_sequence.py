keepplaying="yes"
while keepplaying!="no":
    p1 = input ("Player 1, please choose rock, paper or scissors ")
    p2 = input ("Player 2, please choose rock, paper or scissors ")
    if p1==p2:
         print("That's a tie, would you like to play again?")
    else:
        if p1 =="rock":
            if p2 == "paper":
                print("Congratulations player 2")
            else:
                print ("Congratulations player 1")
        elif p1 =="paper":
            if p2 == "scissors":
                print("Congratulations player 2")
            else:
                print ("Congratulations player 1")
        elif p1 =="scissors":
            if p2 == "rock":
                print("Congratulations player 2")
            else:
                print ("Congratulations player 1")

    keepplaying=input("Would you like to keep playing? (yes/no) ")