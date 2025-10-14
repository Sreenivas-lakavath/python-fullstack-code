# Copyright (c) 2025 Sreenivas-lakavath
# All rights reserved.

# Encryption and Decryption program
import string
import random

char = string.ascii_letters + string.punctuation + string.digits + " "
chars = list(char)
key = chars.copy()
random.shuffle(key)

# encryption
palintext = input("Enter the plain text : ")
encrypted_text = ""

for letter in palintext:
    index = chars.index(letter)
    encrypted_text += key[index]
print(f"The encrypted text is : {encrypted_text}")
    
# decryption
decrypted_text = input("Enter the encrypted text : ")
plain_text = ""
for letter in decrypted_text:
    index = key.index(letter)
    plain_text += chars[index]
print(f"The plain text is : {plain_text}")

print (f" Original plain text is : {palintext}"
        f"\n Encrypted text is : {encrypted_text}"
       f"\n Decrypted text is : {plain_text}")
print("Thank you for using the program")