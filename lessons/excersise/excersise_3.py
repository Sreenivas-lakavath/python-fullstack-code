# this is a python calculator
operator = input ("Enter an operator (+ - )")
num1 = float(input("Enter the first number"))
num2 = float(input("Enter your second number"))

if operator == "+":
    result = num1+num2
    print(result)
elif operator == "-":
    result = num1-num2
    print(result)
elif operator == "*":
    result = num1*num2
    print(result)
elif operator == "/":
    result = num1/num2
    print(result)
else:
    print("please enter a valid operator")