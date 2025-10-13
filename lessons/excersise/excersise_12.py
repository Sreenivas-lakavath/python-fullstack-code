# Copyright (c) 2025 Sreenivas-lakavath
# All rights reserved.

# concession stand program
menu = {
    "burger":5.99,
    "fries":2.99,
    "soda":1.99,
    "salad":4.99,
    "nuggets":3.99
}

cart = []
total = 0


print("Welcome to the concession stand!")
print("-------Here is the menu:-------")
for key in menu.items():
    print(f"{key[0].title()}: ${key[1]}")
    
while True:
    item = input("Enter an item to add to your cart (q to quit): ").lower()
    if item == "q":
        break
    elif menu.get(item) is not None:
        cart.append(item)
        print(f"{item.title()} has been added to your cart.")
    else:
        print("Sorry, we don't have that item.")
print("-------Your cart:-------")
for item in cart:
    print(item.title())
    total += menu[item]
print(f"Your total is: ${total:.2f}")