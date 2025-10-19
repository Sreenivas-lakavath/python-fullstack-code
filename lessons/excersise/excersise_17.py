# Copyright (c) 2025 Sreenivas-lakavath
# All rights reserved.

# credit card validator program
card_number = input("Enter your credit card number :")
card_number = card_number.replace(" ", "")  # Remove spaces if any
if len(card_number) == 16 and card_number.isdigit():
    print("Valid credit card number")
else:
    print("Invalid credit card number")
    
# another way to do it
# if len(card_number) !=16 or not card_number.isdigit():
#     print("Invalid credit card number")
# else:
#     print("Valid credit card number")

# Example of nested if else
# if len(card_number) == 16:
#     if card_number.isdigit():
#         print("Valid credit card number")
#     else:
#         print("Invalid credit card number")
# else:

##     print("Invalid credit card number")

# credit card number should be 16 digits
# should not contain spaces or letters
# sum of the  totals of steps 2 and 3 should be divisible by 10
# step 2 : sum of digits at odd places from the right
# step 3 : sum of double of digits at even places from the right
print("Thank you for using the program")

credit_card_number = "4539 1488 0343 6467"
credit_card_number = credit_card_number[::-1]  # Reverse the credit card number
credit_card_number = credit_card_number.replace(" ", "")
if len(credit_card_number) != 16 or not credit_card_number.isdigit():
    print("Invalid credit card number")
else:
    odd_sum = 0
    even_sum = 0
    for index in range(len(credit_card_number)):
        digit = int(credit_card_number[-(index + 1)])
        if index % 2 == 0:
            odd_sum += digit
        else:
            double_digit = digit * 2
            if double_digit > 9:
                double_digit -= 9
            even_sum += double_digit
    total_sum = odd_sum + even_sum
    if total_sum % 10 == 0:
        print("Valid credit card number")
    else:
        print("Invalid credit card number")