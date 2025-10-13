# Copyright (c) 2025 Sreenivas-lakavath
# All rights reserved.

# fruits = ["apple","orange","banana","coconut"]
# vegetables = ["carrots", "tomoto", "potatoes"]
# meats = ["chicken","fish","turkey"]

# groceries = [fruits,vegetables,meats]
# print(groceries[0][2])

groceries = (("apple","orange","banana","coconut"),
             ("carrots", "tomoto", "potatoes"),
             ("chicken","fish","turkey"))

for collection in groceries:
    for food in collection:
        print(food, end=" ")
        print()
        
# create a num pad

num_pad = ((1,2,3),
           (4,5,6),
           (7,8,9),
           ("*",0,"#"))

for row in num_pad:
    for num in row:
        print(num, end=" ")
    print()