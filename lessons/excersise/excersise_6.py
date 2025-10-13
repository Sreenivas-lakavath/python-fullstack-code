# Copyright (c) 2025 Sreenivas-lakavath
# All rights reserved.
# Validate user input excercise
#username is no more than 12 characters
# username must not contain spaces
#username must contain digits

user_name = input("Enter your name here :")
user_name.find(" ")
user_name.isalpha()
if len(user_name)<12:
    print("your user name can't be less than 12 characters")
elif not user_name.find(" ")== -1:
    print(" no spaces allowed")
elif not user_name.isalpha():
    print("the name should be alphabets")
else:
    print(f"Welcome {user_name}")