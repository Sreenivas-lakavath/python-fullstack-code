# Copyright (c) 2025 Sreenivas-lakavath
# All rights reserved.

# List comprehensions
# A more pythonic way to create lists
# Syntax: [expression for item in iterable if condition == True]
# iterable = a sequence (list, tuple, set, etc.)

squares = [i**2 for i in range(1,11)]
print(squares)
even_squares = [i**2 for i in range(1,11) if i%2==0]
print(even_squares)
cubes = [i**3 for i in range(1,11)]
print(cubes)
odd_cubes = [i**3 for i in range(1,11) if i%2!=0]
print(odd_cubes)
words = ["hello", "world", "python", "is", "awesome"]
lengths = [len(word) for word in words]
print(lengths)
a = [1,2,3,4,5]
b = [6,7,8,9,10]
sums = [x + y for x in a for y in b]
print(sums)
multiples_of_3 = [i for i in range(1,51) if i%3==0]
print(multiples_of_3)
divisible_by_2_and_5 = [i for i in range(1,101) if i%2==0 and i%5==0]
print(divisible_by_2_and_5)
uppercase_words = [word.upper() for word in words]
print(uppercase_words)
lowercase_words = [word.lower() for word in words]
print(lowercase_words)
filtered_words = [word for word in words if "o" in word]
print(filtered_words)
length_greater_than_4 = [word for word in words if len(word)>4]
print(length_greater_than_4)
nested_list = [[1,2,3], [4,5,6], [7,8,9]]
flattened_list = [num for sublist in nested_list for num in sublist]
print(flattened_list)
# conditional expression in list comprehensions
numbers = [i for i in range(1,21)]
parity = ["Even" if i%2==0 else "Odd" for i in numbers]
print(parity)

# create a list of tuples (number, square)
number_square_tuples = [(i, i**2) for i in range(1,11)]
print(number_square_tuples)

# create a list of tuples (word, length)
word_length_tuples = [(word, len(word)) for word in words]
print(word_length_tuples)
# create a list of first letters of each word
first_letters = [word[0] for word in words]
print(first_letters)
# create a list of last letters of each word
last_letters = [word[-1] for word in words]
print(last_letters)
# create a list of words that start with 'p'
words_starting_with_p = [word for word in words if word.startswith('p')]

print(words_starting_with_p)
# create a list of words that end with 'e'
words_ending_with_e = [word for word in words if word.endswith('e')]
print(words_ending_with_e)
# create a list of numbers divisible by 4 or 6
divisible_by_4_or_6 = [i for i in range(1,101) if i%4==0 or i%6==0]
print(divisible_by_4_or_6)
# create a list of numbers that are perfect squares
perfect_squares = [i**2 for i in range(1,11)]
print(perfect_squares)
# create a list of numbers that are perfect cubes
perfect_cubes = [i**3 for i in range(1,11)]
print(perfect_cubes)
# create a list of even numbers squared
even_numbers_squared = [i**2 for i in range(1,21) if i%2==0]
print(even_numbers_squared)
# create a list of odd numbers cubed
odd_numbers_cubed = [i**3 for i in range(1,21) if i%2!=0]
print(odd_numbers_cubed)
# create a list of numbers from 1 to 100 that are divisible by 7
divisible_by_7 = [i for i in range(1,101) if i%7==0]
print(divisible_by_7)
# create a list of numbers from 1 to 100 that are not divisible by 5
not_divisible_by_5 = [i for i in range(1,101) if i%5!=0]
print(not_divisible_by_5)

# create a list of words with length greater than 3
words_length_greater_than_3 = [word for word in words if len(word)>3]
print(words_length_greater_than_3)
# create a list of words with length less than or equal to 4
words_length_less_equal_4 = [word for word in words if len(word)<=4]
print(words_length_less_equal_4)
# create a list of words that contain the letter 'a'
words_containing_a = [word for word in words if 'a' in word]
print(words_containing_a)
# create a list of words that do not contain the letter 'o'
words_not_containing_o = [word for word in words if 'o' not in word]
print(words_not_containing_o)
# create a list of tuples (number, cube)
number_cube_tuples = [(i, i**3) for i in range(1,11)]
print(number_cube_tuples)
# create a list of tuples (word, uppercase)
word_uppercase_tuples = [(word, word.upper()) for word in words]
print(word_uppercase_tuples)
# create a list of tuples (word, lowercase)
word_lowercase_tuples = [(word, word.lower()) for word in words]
print(word_lowercase_tuples)