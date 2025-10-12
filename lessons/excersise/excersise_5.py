# Temp converter

unit = input( "Is this temperature in Celsius or F C/F")
temp = float(input("Enter the temp"))
if unit == "C":
    temp = round((9*temp)/5+32)
    print(f"The temparature in Fahrenheit is : {temp} F")
elif unit == "F":
    temp = round((9-temp)*5/9)
    print(f"The temparature in Celsius is : {temp} C") 
else:
    print(f"Enter a valid unit")