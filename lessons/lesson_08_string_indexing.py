# Copyright (c) 2025 Sreenivas-lakavath
# All rights reserved.

#indexing = access elements of a sequence using [](indexing operator)
# [start : end : step]

credit_card_number = "2345-2345-2345-5634-2345"
print(credit_card_number[0])
print(credit_card_number[0:4]) #ending number would be exclusive
print(credit_card_number[6:10])
print(credit_card_number[6:]) #don't include ending for all info
print(credit_card_number[-1]) # reverse order
print(credit_card_number[::3]) # prints every third character


last_digits= credit_card_number[-4:]
print(f"XXXXX-XXXX-XXXXX-{last_digits}")

credit_card_number = credit_card_number[::-1] # reverse string
print(credit_card_number)

 