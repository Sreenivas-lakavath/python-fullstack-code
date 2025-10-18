# Copyright (c) 2025 Sreenivas-lakavath
# All rights reserved.

# keyword arguments in functions
# defining a function that uses key arguments
# function to display information about a book
def display_book_info(title, author, year_published):
    print(f"Title: {title}")
    print(f"Author: {author}")
    print(f"Year Published: {year_published}")
# calling the function using key arguments
display_book_info(title="To Kill a Mockingbird", author="Harper Lee", year_published=1960)
display_book_info(author="George Orwell", title="1984", year_published=1949)
display_book_info(year_published=2003, title="The Da Vinci Code", author="Dan Brown")
# function to create a user profile
def create_user_profile(username, email, age):
    print(f"Username: {username}")
    print(f"Email: {email}")
    print(f"Age: {age}")
# calling the function using key arguments
create_user_profile(username="john_doe", email="GMAIL.COM", age=28)
create_user_profile(age=35, username="jane_smith", email="YAHOO.COM")
create_user_profile(email="OUTLOOK.COM", age=22, username="alice_wonderland")
# function to calculate the area of a rectangle
def calculate_area(length, width):
    area = length * width
    print(f"Area of the rectangle: {area}")
# calling the function using key arguments
calculate_area(length=5, width=10)
calculate_area(width=7, length=3)
calculate_area(length=4.5, width=2.8)

# compound interest calculator
A = P (1 + r/n) ^ nt
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the annual interest rate (in %): ")) / 100
times_compounded = int(input("Enter the number of times interest is compounded per year: "))
years = int(input("Enter the number of years the money is invested for: "))
amount = principal * (1 + rate / times_compounded) ** (times_compounded * years)
print(f"The amount after {years} years is: {amount:.2f}")
# shopping cart game
cart = []
def add_to_cart(item, quantity):
    cart.append((item, quantity))
    print(f"Added {quantity} of {item} to the cart.")
def view_cart():
    print("Your shopping cart contains:")
    for item, quantity in cart:
        print(f"{quantity} of {item}")
while True:
    action = input("Would you like to add an item to the cart or view the cart? (add/view/quit): ").lower()
    if action == "add":
        item = input("Enter the item name: ")
        quantity = int(input("Enter the quantity: "))
        add_to_cart(item, quantity)
    elif action == "view":
        view_cart()
    elif action == "quit":
        print("Thank you for shopping with us!")
        break
    else:
        print("Invalid action. Please choose 'add', 'view', or 'quit'.")