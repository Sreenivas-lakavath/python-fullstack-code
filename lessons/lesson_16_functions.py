# Copyright (c) 2025 Sreenivas-lakavath
# All rights reserved.

# functions in python
# a function is a block of code which only runs when it is called
# you can pass data, known as parameters, into a function
# a function can return data as a result

def this_is_a_function():
    print("this is a function")
this_is_a_function()  # calling a function
def greet_user(name):
    print(f"Hello {name}, welcome to python")
greet_user("Sreenivas")
greet_user("Lakavath")
def add_numbers(num1, num2):
    return num1 + num2
result = add_numbers(5, 10)
print(result)
result = add_numbers(20, 30)
print(result)
def multiply_numbers(num1, num2):
    return num1 * num2
result = multiply_numbers(5, 10)
print(result)
result = multiply_numbers(20, 30)
print(result)
# default parameter value
def power(base, exponent=2):
    return base ** exponent
result = power(5)
print(result)
result = power(5, 3)
print(result)
# keyword arguments
def divide_numbers(num1, num2):
    return num1 / num2
result = divide_numbers(num2=10, num1=5)
print(result)
result = divide_numbers(20, 4)
print(result)
# variable scope
x = 10  # global variable
def print_x():
    y = 5  # local variable
    print(f"x inside function: {x}")
    print(f"y inside function: {y}")
print_x()
print(f"x outside function: {x}")
# print(f"y outside function: {y}")  # this will cause an error 
# because y is not defined outside the function
# lambda functions
add = lambda a, b: a + b
result = add(5, 10)
print(result)
multiply = lambda a, b: a * b
result = multiply(5, 10)
print(result)   
# built-in functions
def use_built_in_functions():
    numbers = [5, 2, 9, 1, 5, 6]
    print(f"Original list: {numbers}")
    print(f"Sorted list: {sorted(numbers)}")
    print(f"Length of list: {len(numbers)}")
    print(f"Maximum value: {max(numbers)}")
    print(f"Minimum value: {min(numbers)}")
use_built_in_functions()    
# recursive functions
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
result = factorial(5)
print(result)
result = factorial(7)
print(result)   
# docstrings
def square(num):
    """This function returns the square of a number."""
    return num ** 2
print(square(5))
print(square.__doc__)
print(help(square))
# importing functions from modules
import math
result = math.sqrt(16)
print(result)
result = math.factorial(5)
print(result)
from math import pow, ceil
result = pow(2, 3)
print(result)
result = ceil(4.2)
print(result)   
# creating your own module
# create a file named my_module.py with the following content:
# def greet(name):
#     return f"Hello, {name}!"
# then you can import and use it as follows:
# from my_module import greet
# print(greet("Sreenivas"))