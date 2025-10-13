# Copyright (c) 2025 Sreenivas-lakavath
# All rights reserved.

# Number Guessing Game
import random

lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num, highest_num)
guesses = 0
is_running = True


print("****** Welcome to the Number Guessing Game! ******")
print(f"I'm thinking of a number between {lowest_num} and {highest_num}.")
print("Try to guess the number!")

while is_running:
    guess = int(input("Make a guess: "))
    if guess < lowest_num or guess > highest_num:
        print(f"Please guess a number between {lowest_num} and {highest_num}.")
        continue
    guesses += 1
    if guess < answer:
        print("Too low.")
    elif guess > answer:
        print("Too high.")
    else:
        is_running = False
        print(f"Congratulations! You've guessed the number {answer} in {guesses} tries.")