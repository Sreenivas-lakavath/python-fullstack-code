# Copyright (c) 2025 Sreenivas-lakavath
# All rights reserved.

# if = Do some code only IF some condition is True
# Else do something else

age = float(input("Hi sir enter your age here: "))
if age >= 18:
    print(" You're signed up!")
elif age >= 10:
    print( "You must be 18 to sign up")
elif age >= 100:
    print( "You are too old sign up")
elif age >= 5:
    print( "You must be 18 to sign up")
elif age <= 0:
    print( "you are not born yet")
# else:
#     print(f" Sorry you must grow{age}")

# lets create a food game

response = input(" Would you like food? Say Yes or No? :")
if response == "yes":
    print("You have some food for you")
    
else:
    print(" No food for you")
    
# name game
name = input( " enter your name here :")

if name == "":
    print("You have no name")
else:
    print(f"Hi {name}")
    
# lets try now with bools

for_sale = True

if for_sale:
    print("Ye you can have it")
else:
    print(" you not allwoed now")