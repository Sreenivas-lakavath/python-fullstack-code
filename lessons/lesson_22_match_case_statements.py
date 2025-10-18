# Copyright (c) 2025 Sreenivas-lakavath
# All rights reserved.

# match case statements in python
# match case is similar to switch case in other languages
# available in python 3.10 and above

# example 1
def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"
print(http_error(400))
print(http_error(404))
print(http_error(418))
print(http_error(500))

# example 2
def greet_user(role):
    match role:
        case "admin":
            return "Hello Admin, welcome back!"
        case "user":
            return "Hello User, welcome back!"
        case "guest":
            return "Hello Guest, please sign up!"
        case _:
            return "Hello, welcome!"
print(greet_user("admin"))
print(greet_user("user"))
print(greet_user("guest"))
print(greet_user("other"))

# example 3
def day_of_week(day):
    match day:
        case 1:
            return "Monday"
        case 2:
            return "Tuesday"
        case 3:
            return "Wednesday"
        case 4:
            return "Thursday"
        case 5:
            return "Friday"
        case 6:
            return "Saturday"
        case 7:
            return "Sunday"
        case _: # default case or wildcard case
            return "Invalid day"
print(day_of_week(1))
print(day_of_week(5))
print(day_of_week(8))

# example 4

def is_weekend(day):
    match day:
        case "Saturday" | "Sunday":
            return True
        case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
            return False
        case _:
            return "Invalid day"    
        
print(is_weekend("Saturday"))
print(is_weekend("Wednesday"))
print(is_weekend("Funday")) 
# example 5
def calculate_operation(op, a, b):
    match op:
        case "add":
            return a + b
        case "subtract":
            return a - b
        case "multiply":
            return a * b
        case "divide":
            return a / b
        case _:
            return "Invalid operation"
print(calculate_operation("add", 5, 3))
print(calculate_operation("subtract", 5, 3))
print(calculate_operation("multiply", 5, 3))
print(calculate_operation("divide", 5, 0))
print(calculate_operation("modulus", 5, 3))

# output:
# Bad request
# Not found
# I'm a teapot
# Something's wrong with the internet
# Hello Admin, welcome back!
# Hello User, welcome back!
# Hello Guest, please sign up!
# Hello, welcome!
# Monday
# Friday
# Invalid day
# True
# False
# Invalid day
# 8
# 2
# 15
# division by zero error
# Invalid operation 