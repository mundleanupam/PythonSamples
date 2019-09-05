import random


# Algorithm
# Player 1 - Manually accept input
# Player 2 - Computer to get random integer between 1and 3
# Rock vs paper-> paper wins
# Rock vs scissor-> Rock wins
# paper vs scissor-> scissor wins.
# Count the number of wins and whoever reaches first 3 wins is the winner

player_win_count = 0
comp_win_count = 0

print """Game of Rock/Paper/Scissor Rules - 
    Rock vs paper-> paper wins
    Rock vs scissor-> Rock wins
    paper vs scissor-> scissor wins."""

while player_win_count < 3 and comp_win_count < 3:
    choice_dict = {1: "ROCK", 2: "PAPER", 3: "Scissor"}

    print ""

    print "Select 1.Rock 2.Paper 3.Scissor"

    choice = int(input("User Turn: "))
    while choice > 3 or choice < 1:
        choice = int(input("Enter valid input: "))
    if choice in choice_dict:
        print("User choice is: " + choice_dict.get(choice))
    else:
        print("Choose 1.Rock 2.Paper 3.Scissor")

    comp_choice = random.randint(1, 3)
    if comp_choice in choice_dict:
        print("Computer choice is: " + choice_dict.get(comp_choice))

    if (choice == 2 and comp_choice == 1) or (choice == 1 and comp_choice == 2):
        print(choice_dict.get(2) + " Wins!")
        if choice == 2:
            player_win_count += 1
        else:
            comp_win_count += 1
    elif (choice == 1 and comp_choice == 3) or (choice == 3 and comp_choice == 1):
        print(choice_dict.get(1) + " Wins!")
        if choice == 1:
            player_win_count += 1
        else:
            comp_win_count += 1
    elif (choice == 2 and comp_choice == 3) or (choice == 3 and comp_choice == 2):
        print(choice_dict.get(3) + " Wins!")
        if choice == 3:
            player_win_count += 1
        else:
            comp_win_count += 1
    else:
        print("It is a Tie")

if player_win_count > comp_win_count:
    print ("USER WINS THE ROUND")
else:
    print ("COMPUTER WINS THE ROUND")






