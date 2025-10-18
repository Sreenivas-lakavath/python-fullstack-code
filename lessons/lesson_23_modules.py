# Copyright (c) 2025 Sreenivas-lakavath
# All rights reserved.

# module lesson
# modules are files containing python code
# we can import the code from one module to another module
# this helps us to reuse the code
# we can import standard library modules or custom modules

import lessons.excersise.excersise_3
import lessons.excersise.excersise_5
import lessons.excersise.excersise_2    
# when we import a module the code inside the module is executed
# to avoid this we can use the if __name__ == "__main__": block
# this block ensures that the code inside it is only executed when the module is run directly
# and not when it is imported
def main():
    print("This is the main function in lesson_23_modules.py")
if __name__ == "__main__":
    main()
# we can also import specific functions or variables from a module
from lessons.excersise.excersise_2 import friends, apples
print(f"friends: {friends}")
print(f"apples: {apples}")
# we can also give an alias to a module or a function
import lessons.excersise.excersise_3 as calculator
# now we can use calculator to access the functions and variables in excersise_3
# for example if excersise_3 had a function called add we could call it like this
# result = calculator.add(5, 10)
# print(result)
# this is useful to avoid name conflicts or to shorten long module names

# we can also use from ... import ... as to give an alias to a specific function or variable
from lessons.excersise.excersise_2 import friends as num_friends
print(f"num_friends: {num_friends}")
# this is useful to avoid name conflicts or to shorten long names
# that's it for modules in python

import math
print(math.pi)
print(math.sqrt(16))

import random
print(random.randint(1, 10))
print(random.choice(['apple', 'banana', 'cherry']))
import datetime
now = datetime.datetime.now()
print(now)
print(now.strftime("%Y-%m-%d %H:%M:%S"))
# these are some of the standard library modules in python
# there are many more modules available in the standard library
# you can find the full list here: https://docs.python.org/3/library/