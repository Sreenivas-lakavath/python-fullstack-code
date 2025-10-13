# Copyright (c) 2025 Sreenivas-lakavath
# All rights reserved.

# random number generator
import random

low = int(input("Enter the lowest number: "))
high = int(input("Enter the highest number: "))
count = int(input("How many random numbers do you want to generate? "))
for x in range(0, count): # range(start, stop, step)
    print(random.randint(low, high)) # generate a random number between low and high
    
# Number guessing game
low = 1
high = 10
guesses = 0
secret_number = random.randint(low, high) # generate a random number between low and high

while True:
    user_guess = int(input(f"Enter your guess ({low}-{high}): "))
    guesses += 1 # increment the number of guesses
    if user_guess < low or user_guess > high: # check if the guess is out of bounds
        print("Your guess is out of bounds. Try again.")
    elif user_guess < secret_number:
        print("Too low! Try again.")
    elif user_guess > secret_number: # elif user_guess > secret_number
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You guessed the number {secret_number} in {guesses} guesses.")
        break