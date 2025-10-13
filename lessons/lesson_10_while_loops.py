# while loop = execute some code WHILE some condition remains true
name = input("Enter you name: ")
if name == "":
    print("You didn't enter anything")
else:
    print(f"Hello {name}")
    
# lets do the same with while loop
user_name = ""
while user_name == "":
    user_name = input("Enter your name: ")
print(f"Hello {user_name}")

# lets do a password checker
password = "1234"
user_password = ""
while user_password != password:
    user_password = input("Enter your password: ")
print("You are logged in")
# lets do a number guessing game
secret_number = 5
user_guess = 0
while user_guess != secret_number:
    user_guess = int(input("Enter your guess (1-10): "))
print("You win!")
# lets do a menu
menu = """
1. Say Hello
2. Say Goodbye
3. Quit
"""
user_input = ""
while user_input != "3":
    print(menu)
    user_input = input("Enter your choice: ")
    if user_input == "1":
        print("Hello!")
    elif user_input == "2":
        print("Goodbye!")
    elif user_input == "3":
        print("Quitting...")
    else:
        print("Invalid choice, please try again.")
print("You have exited the menu.")

# food ordering system
menu = """
1. Pizza - $10
2. Burger - $5
3. Salad - $7
4. Quit
"""
total = 0
user_input = ""
while user_input != "4":
    print(menu)
    user_input = input("Enter your choice: ")
    if user_input == "1":
        total += 10
        print("You ordered a Pizza.")
    elif user_input == "2":
        total += 5
        print("You ordered a Burger.")
    elif user_input == "3":
        total += 7
        print("You ordered a Salad.")
    elif user_input == "4":
        print("Quitting...")
    else:
        print("Invalid choice, please try again.")
print(f"Your total is: ${total}")
print("Thank you for your order!")

# enter a avalid number
num = int(input("Enter a number between 1 and 10: "))
while num < 1 or num > 10:
    print("Invalid number, please try again.")
    num = int(input("Enter a number between 1 and 10: "))
print(f"You entered: {num}")