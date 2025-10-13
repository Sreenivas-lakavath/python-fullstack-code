# Copyright (c) 2025 Sreenivas-lakavath
# All rights reserved.
# for loops = a statement that will execute it's block of code
# a limited amount of times [ fixed iteration ]

# for x in range(1,11): # 1,2,3,4,5,6,7,8,9,10
#     print(x)
# print("Wishing you a happy thanksgiving")
# # reverse order
# for x in range(10,0,-1): # 10,9,8,7,6,5,4,3,2,1
#     print(x)
# print("Happy new year")
# # even numbers
# for x in range(0,21,2): # 0,2,4,6,8,10,12,14,16,18,20
#     print(x)
# print("Happy even year")
# # odd numbers
# for x in range(1,20,2): # 1,3,5,7,9,11,13,15,17,19
#     print(x)
# print("Happy odd year")
# # lets do a power of 2 table
# for x in range(1,11):
#     print(f"2 to the power of {x} is {2**x}")
# print("Happy power of 2 year")
# # lets do a multiplication table
# number = int(input("Enter a number to multiply: "))
# for x in range(1,11):
#     print(f"{number} x {x} = {number * x}")
# print("Happy multiplication year")
# # lets do a nested loop
# for x in range(1,6): # outer loop
#     for y in range(1,6): # inner loop
#         print(f"({x}, {y})")
# print("Happy nested loop year")
# # lets do a list of items
# fruits = ["apple", "banana", "cherry", "date"]
# for fruit in fruits:
#     print(fruit)
# print("Happy fruit year")
# # lets do a sum of numbers
# total = 0
# for x in range(1,101):
#     total += x
# print(total)
# print("Happy sum year")

# continue, break, pass
# for x in range(1,21):
#     if x == 13:
#         print("Unlucky number")
#         continue # skips the rest of the code
#     print(x)
# print("Happy continue year")
# for x in range(1,21):
#     if x == 13:
#         print("Unlucky number")
#         break # exits the loop
#     print(x)
# print("Happy break year")
for x in range(1,21):
    if x == 13: # skips the rest of the code
        break
    else:
        print(x)
        
## Nested loops
# nested loops = a loop inside another loop
# outer loop = the loop that contains the inner loop
# inner loop = the loop that is inside the outer loop

for x in range(1,11): # outer loop
    for y in range(1,11): # inner loop
        print(f"{x} x {y} = {x * y}")
    print("----------")
print("Happy nested loop year")

for x in range(1,6): # out
    print (x, end=" ")

for x in range(3):
    for y in range(1,101):
        print(y, end=" ")
    print()
    # lets draw a rectangle
rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of columns: "))
symbol = input("Enter a symbol to use: ")
for x in range(rows):
    for y in range(columns):
        print(symbol, end=" ")
    print()
print("Happy rectangle year")