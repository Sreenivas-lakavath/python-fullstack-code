# Copyright (c) 2025 Sreenivas-lakavath
# All rights reserved.

# shopping cart program

foods = []
prices = []
total = 0

while True:
    food = input(" Enter a food to bug (q to quite)")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price of a {food}: $"))
        foods.append(food)
        prices.append(price)
print("----------Your shopping Cart -----------")

for food in foods:
    print(food, end=" ")
    
for price in prices:
    total += price
    
print()
print(f" YOur total is : ${total}")