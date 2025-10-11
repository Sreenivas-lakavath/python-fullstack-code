# lets take inputs using input

name = input( " Enter your name here : ")
age =  int(input(" you can enter your age here :"))
age = age + 1
 
print(f"Hello {name}")
print(f"Hello {age}")

# mad libs game 
adjective1 = input("Enter an adjective : ")
noun = input("Enter a noun : ")
adjective2 = input("Enter an adjective : ")
adjective3 = input("Enter an adjective : ")
verb = input("Enter an adjective : ")

print(f"Today I went to a {adjective1} zoo.")
print(f"In an exhibit, I saw {noun}")
print(f"{noun} was {adjective2} and {verb}ing" )
print(f"I was {adjective3}")

# Area calculation game
lenth = float(input("Enter the length of a rectangle : "))
width = float(input("Enter the width : "))
height = float(input("Enter an height : "))

area = width * lenth

print(f"the area is : {area} cm^3")

# shopping cart game

item =str(input("what would you like to buy : "))
price = float(input("what is the price: "))
quality = int(input("Enter the quality: "))

total = price * quality
print(f" you have bough {quality} x {item}/s")
print(f" your total is {total}")