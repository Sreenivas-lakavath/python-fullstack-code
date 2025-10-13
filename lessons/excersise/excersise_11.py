# Copyright (c) 2025 Sreenivas-lakavath
# All rights reserved.

# Create a quiz game with python
print("Welcome to the quiz game")
playing = input("Do you want to play? ")
questions = ("What is the capital of India? \n a. Delhi \n b. Mumbai \n c. Chennai\n",
"What is the capital of USA? \n a. Washington DC \n b. New York \n c. Los Angeles\n",
"What is the capital of UK? \n a. London \n b. Manchester \n c. Birmingham\n",
"What is the capital of France? \n a. Paris \n b. Lyon \n c. Marseille\n",
"What is the capital of Germany? \n a. Berlin \n b. Munich \n c. Frankfurt\n")
options = ("a","a","a","a","a")
answers = ("a","b","c","a","a")
guesses = []
score = 0

for question in questions: # iterate through the questions tuple
    print("-------------------")
    print(question)
    guess = input("Enter (a, b, or c): ")
    guesses.append(guess) # add the guess to the guesses list
    correct_answer = options[questions.index(question)] # get the correct answer from the options tuple
    if guess == correct_answer: # compare the guess with the correct answer
        score += 1 # increment the score by 1
        print("CORRECT!") # print correct
    else: # if the guess is wrong
        print("WRONG!") # print wrong
        print(f"The correct answer is {correct_answer}") # print the correct answer
        
print("-------------------")
print("RESULTS")
print("-------------------")
print("Answers: ", end="")
for answer in answers: # iterate through the answers tuple
    print(answer, end=" ") # print the answers
print()
print("Guesses: ", end="")
for guess in guesses: # iterate through the guesses list
    print(guess, end=" ") #print the guesses
print()
print(f"Your score is {score}/{len(questions)}") # print the score
percentage = int((score/len(questions))*100) # calculate the percentage
print(f"Your percentage is: {percentage}%") # print the percentage