# Copyright (c) 2025 Sreenivas-lakavath
# All rights reserved.

# string = a series of characters
name = input("Enter your name: ")
# result = len(name)
result = name.find(" ") # find always returns the first occurance of the character
# rfind() always returns the last occurance of the character
# if no results found, find method returns -1
# name.capitalize() changes to first letter to capital
# name.upper() turns all into upper case
# name = name.upper() overrides the existing
#name = name.lower()
# result = name.isdigit()
# result = name.isalpha() returns true if only characters without spaces or numbers
print(result)# the indexes always starts with 0
phone_number = "343-2345-2345--2345-234"
#phone_number.count("-")
#phone_number.replace("-"," ") we can ovverride 
#for more info print(help(str))