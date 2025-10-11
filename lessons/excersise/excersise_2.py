friends = 0
friends = friends +1

#agmented text
friends -= 3
print(friends)

apples = 0
apples *=3
print(apples)


balls = 0
balls /= 2
print(balls)

tables = 0
tables **= 2
print(tables)
god = 5
god %= 2 
print(god)

# built-in functions

x = 3.14
y = 4
z = 5
result = round(x)
print(result)

# absoulute value
x = 4
y = -3
absolute = abs(y)
print(absolute)

absolute = max(x,y)
print(f"the max is {absolute}")

absolute = min(x,y)
print(absolute)

# we have constants 
# we must import math

import math
print(math.pi)
print(math.e)

x = 9
result = math.sqrt(x)
print(result)
result = math.floor(x)
print(result)

result = math.ceil(x)
print(result)


# lets calculate the circumference 

radius = float(input ("enter the radius here: "))
circumference = 2 *math.pi *radius
print (f"the cirle {circumference}")

# lets calculate the circle area
radius = float(input ("enter the area here: "))
circumference = 2 *math.pi * pow(radius,2)
print (f"the cirle {circumference}")