# Copyright (c) 2025 Sreenivas-lakavath
# All rights reserved.

# banking app program

balance = 0
while True:
    print(" Welcome to the banking app")
    print(" 1. Deposit")
    print(" 2. Withdraw")
    print(" 3. Check Balance")
    print(" 4. Exit")
    
    choice = input(" Enter your choice (1-4): ")
    
    if choice == "1":
        amount = float(input(" Enter amount to deposit: $"))
        balance += amount
        print(f" Deposited: ${amount}")
        
    elif choice == "2":
        amount = float(input(" Enter amount to withdraw: $"))
        if amount > balance:
            print(" Insufficient funds")
        else:
            balance -= amount
            print(f" Withdrew: ${amount}")
            
    elif choice == "3":
        print(f" Current Balance: ${balance}")
        
    elif choice == "4":
        print(" Exiting the banking app. Goodbye!")
        break
        
    else:
        print(" Invalid choice. Please try again.")
    print()  # Print a newline for better readability
    
    
    # another way to do the same program
# while True:
#     print(" Welcome to the banking app")
#     print(" 1. Deposit")
#     print(" 2. Withdraw")
#     print(" 3. Check Balance")
#     print(" 4. Exit") 
#     choice = input(" Enter your choice (1-4): ")
#     if choice not in ["1", "2", "3", "4"]:
#         print(" Invalid choice. Please try again.")
#         continue
#     if choice == "4":
#         print(" Exiting the banking app. Goodbye!")
#         break
#     if choice == "1":
#         amount = float(input(" Enter amount to deposit: $"))
#         balance += amount
#         print(f" Deposited: ${amount}")
#     elif choice == "2":
#         amount = float(input(" Enter amount to withdraw: $"))
#         if amount > balance:
#             print(" Insufficient funds")
#         else:
#             balance -= amount
#             print(f" Withdrew: ${amount}")
#     elif choice == "3":
#         print(f" Current Balance: ${balance}")
#     print()  # Print a newline for better readability