# Copyright (c) 2025 Sreenivas-lakavath
# All rights reserved.

# Conditonal expression = A one-line shortcut for the if-else statement( ternary operator)
# print or asssign one of two values based on a condition
# X if condtion else Y

num = 60
a =6
b = 8
age = 13
temperature = 30
user_role = "ADMIN"
# print ("postive " if num> 0 else "Negative")
# result = "EVEN" if num % 2 == 0 else "ODD"
# max_num = a if a >b else b
# min_num = a if a < b else b
# status = "Adult" if age >= 18 else "Child"
# weather = "HOT" if temperature >20 else "COLD"
# print(weather)
access_level = "FULL ACCESS" if user_role == "ADMIN" else "LIMITED ACCESS"
print(access_level)