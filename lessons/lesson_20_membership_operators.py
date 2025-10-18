# Copyright (c) 2025 Sreenivas-lakavath
# All rights reserved.

# Membership operators in Python
# 'in' and 'not in' are the membership operators in Python.
# They are used to test whether a sequence (such as a string, list, or tuple) contains a particular element.
# 'in' returns True if the element is found in the sequence, otherwise it returns False.
# 'not in' returns True if the element is not found in the sequence, otherwise it returns False.
# Example usage:
my_list = [1, 2, 3, 4, 5]
print(3 in my_list)      # Output: True
print(6 in my_list)      # Output: False
print(3 not in my_list)  # Output: False
print(6 not in my_list)  # Output: True
my_string = "Hello, World!"
print("H" in my_string)      # Output: True
print("z" in my_string)      # Output: False
print("H" not in my_string)  # Output: False
print("z" not in my_string)  # Output: True
# Membership operators are commonly used in conditional statements to check for the presence or absence of elements in sequences.
# Example with conditional statements:
if 3 in my_list:
    print("3 is in the list")
if "z" not in my_string:
    print("'z' is not in the string")
    
# Output:
# True
# False
# False
# True
# True
# False
# False
# True
# 3 is in the list
# 'z' is not in the string

students = ["sreenivas", "lakavath", "sravanthi", "lakshmi"]
name = input("Enter your name:")
if name in students:
    print(f"welcome back {name}")
else:
    print(f"sorry {name} you are not allowed")
    
# Output:
# Enter your name:sreenivas
# welcome back sreenivas
# Enter your name:john
# sorry john you are not allowed

# Another example
password = input("Enter your password:")
if " " in password:
    print("password can't contain spaces")
else:
    print("password accepted")
    
    
# Output:
# Enter your password:my password
# password can't contain spaces
# Enter your password:mypassword
# password accepted

scholarship_students = ["alice", "bob", "charlie"]
applicant_name = input("Enter the applicant's name: ")
if applicant_name not in scholarship_students:
    print(f"Sorry {applicant_name}, you are not eligible for the scholarship.")
else:
    print(f"Congratulations {applicant_name}, you are eligible for the scholarship!")
    
# Output:
# Enter the applicant's name: dave
# Sorry dave, you are not eligible for the scholarship.
# Enter the applicant's name: alice
# Congratulations alice, you are eligible for the scholarship!
# Check if a character is in a string
text = "The quick brown fox jumps over the lazy dog"
char_to_check = input("Enter a character to check: ")
if char_to_check in text:
    print(f"The character '{char_to_check}' is present in the text.")
else:
    print(f"The character '{char_to_check}' is not present in the text.")
    
# Output:
# Enter a character to check: q
# The character 'q' is present in the text.
# Enter a character to check: z
# The character 'z' is present in the text. 

# another example

Grades = {"sreenivas": "A", "lakavath": "B", "sravanthi": "A", "lakshmi": "C"}
student_name = input("Enter the student's name: ")
if student_name in Grades:
    print(f"{student_name}'s grade is {Grades[student_name]}")
else:
    print(f"No grade found for {student_name}")
    
# Output:
# Enter the student's name: sreenivas
# sreenivas's grade is A
# Enter the student's name: john
# No grade found for john
# Check membership in a list of dictionaries
employees = [{"name": "Alice", "id": 101}, {"name": "Bob", "id": 102}, {"name": "Charlie", "id": 103}]
employee_name = input("Enter the employee's name: ")
if any(emp["name"] == employee_name for emp in employees):
    print(f"Employee {employee_name} found.")
else:
    print(f"Employee {employee_name} not found.")   