# Copyright (c) 2025 Sreenivas-lakavath
# All rights reserved.
# email slicer excersise

email = input("enter your email")
# index = email.index("@")

username = email[:email.index("@")]
domain = email[email.index("@")+1:] # if you wanna exclude the @ use [ index + 1:]

print(f"Your username is {username} and domain is {domain}")