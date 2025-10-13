# Copyright (c) 2025 Sreenivas-lakavath
# All rights reserved.
# weight converter
weight = float(input("enter your weight:"))
startunit = input("Kilograms,Pounds or stone? (K, L or S)")
endunit = input("what would you like to convert to? (K, L or S)")

if startunit == "K":
    if endunit == "L":
        weight = weight * 2.205
        unit = "Lbs."
        print(f"Your weight is:{round(weight, 1)}{unit}")
    if endunit == "K":
        weight = weight
        unit = "Kgs."
        print(f"Your weight is:{round(weight, 1)}{unit}")
    if endunit == "S":
        weight = weight / 6.35029318
        unit = "Stone"
        print(f"Your weight is:{round(weight, 1)}{unit}")

if startunit == "L":
    if endunit=="L" :
        weight = weight
        unit = "Lbs."
        print (f"Your weight is:{round(weight,1)}{unit}")
    if endunit=="K" :
        weight = weight/2.205
        unit = "Kgs."
        print (f"Your weight is:{round(weight,1)}{unit}")
    if endunit=="S" :
        weight = weight/14
        unit = "Stone"
        print (f"Your weight is:{round(weight,1)}{unit}")

if startunit == "S":
    if endunit=="L" :
        weight = weight*14
        unit = "Lbs."
        print (f"Your weight is:{round(weight,1)}{unit}")
    if endunit=="K" :
        weight = weight*6.35029318
        unit = "Kgs."
        print (f"Your weight is:{round(weight,1)}{unit}")
    if endunit=="S" :
        weight = weight
        unit = "Stone"
        print (f"Your weight is:{round(weight,1)}{unit}")
else:
    print(f"{endunit} was not valid")