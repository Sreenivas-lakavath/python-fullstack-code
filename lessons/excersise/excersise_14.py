# Copyright (c) 2025 Sreenivas-lakavath
# All rights reserved.

# Rock paper scissors game
import random

options = ["rock", "paper", "scissors"]
player_wins = None
computer_wins = random.choice(options) # computer choice from the list

while player_wins not in options:
    player_wins = input("Enter rock, paper or scissors: ").lower()
    if player_wins not in options:
        print("Invalid choice, please try again.")
    elif player_wins == computer_wins:
        print("It's a tie!")
    elif (player_wins == "rock" and computer_wins == "scissors") or \
         (player_wins == "paper" and computer_wins == "rock") or \
         (player_wins == "scissors" and computer_wins == "paper"):
        print("You win!")
    else:
        print("Computer wins!  ****")
        
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again == "yes":
            player_wins = None  # Reset player choice for a new game
            computer_wins = random.choice(options)  # New computer choice
        else:
            print("Thanks for playing!")
            break
print(f"Computer chose: {computer_wins}")
print(f"You chose: {player_wins}")