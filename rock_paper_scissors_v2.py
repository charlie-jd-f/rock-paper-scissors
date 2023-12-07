import random

# list to store possible options for the computer to pick from
options = ["rock","paper","scissors"]

# create variables to store number of games, wins, loses and draws
# and percentage
wins = 0
draws = 0
loses = 0
games = 0
percentage = 0

# create loop so the game can play multiple types
play_again = "yes"

while True:
    games += 1
    if play_again == "yes":
        # computer selects a choice at random
        comp_choice = options[random.randint(0,2)]

        # user inputs their choice, place in lowercase
        user_choice = input("Enter your choice (rock/paper/scissors): \n").lower()
        print()

        #while loop to ensure user is inputting correct option
        while True:
            if user_choice in options:
                break
            else:
                print("Error: Input not recognised. Please type in 'rock','paper'" \
                    ",'scissors'.")
                user_choice = user_choice = input("Enter your choice (rock/paper/scissors): ").lower()

        # check for a win/lose/draw
        if user_choice == comp_choice:
            print("This is a draw")
            draws += 1

        elif user_choice == "rock":
            if comp_choice == "scissors":
                wins += 1
                print(f"You Win! {user_choice} beats {comp_choice}")

            else:
                loses += 1
                print(f"You lose! {comp_choice} beats {user_choice}")

        elif user_choice == "scissors":
            if comp_choice == "paper":
                wins += 1
                print(f"You Win! {user_choice} beats {comp_choice}")

            else:
                loses += 1
                print(f"You lose! {comp_choice} beats {user_choice}")
       
        elif user_choice == "paper":
            if comp_choice == "rock":
                wins += 1
                print(f"You Win! {user_choice} beats {comp_choice}")

            else:
                loses += 1
                print(f"You lose! {comp_choice} beats {user_choice}")

        print()
        play_again = input("Would you like to play again? \n")
        print("=============================")

    elif play_again == "no":
        break

    else:
        print("Error: Input not recognised. Please type 'yes' or 'no'.")
        play_again = input("Would you like to play again? \n")
        
# calculate win percentage
percentage = (wins/games)*100

print("\n Thank you for playing! \n")
print("===========")
print("Stats:")
print("Games played",games)
print("Wins:",wins)
print("Draws:",draws)
print("Loses:",loses)
print("Win %:",percentage)
print("===========")
