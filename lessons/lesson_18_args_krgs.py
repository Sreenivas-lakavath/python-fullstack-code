# copyright @Sreenivas-lakavath 
# All rights reserved.

# arguments and keyword arguments
# *args and **krgs
def add_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total
result = add_numbers(1, 2, 3, 4, 5)
print(result)

result = add_numbers(10, 20, 30)
print(result)
def print_user_info(**krgs):
    for key, value in krgs.items():
        print(f"{key}: {value}")
print_user_info(name="Sreenivas", age=25, city="New York")
print_user_info(name="Lakavath", age=30, country="USA", profession="Engineer")
def mixed_function(arg1, arg2, *args, **krgs):
    print(f"arg1: {arg1}")
    print(f"arg2: {arg2}")
    print("args:")
    for arg in args:
        print(f"  {arg}")
    print("krgs:")
    for key, value in krgs.items():
        print(f"  {key}: {value}")
mixed_function(1, 2, 3, 4, 5, name="Sreenivas", age=25)
mixed_function("Hello", "World", 10, 20, 30, city="New York", country="USA")
# unpacking arguments
def multiply_numbers(a, b, c):
    return a * b * c
numbers = (2, 3, 4)
result = multiply_numbers(*numbers)
print(result)
numbers_dict = {'a': 5, 'b': 6, 'c': 7}
result = multiply_numbers(**numbers_dict)
print(result)

# combination of all
def complex_function(arg1, arg2, *args, **krgs):
    print(f"arg1: {arg1}")
    print(f"arg2: {arg2}")
    print("args:")
    for arg in args:
        print(f"  {arg}")
    print("krgs:")
    for key, value in krgs.items():
        print(f"  {key}: {value}")
complex_function(1, 2, 3, 4, 5, name="Sreenivas", age=25)
complex_function("Hello", "World", 10, 20, 30, city="New York", country="USA")
def another_function(a, b, c=1, *args, **krgs):
    print(f"a: {a}")
    print(f"b: {b}")
    print(f"c: {c}")
    print("args:")
    for arg in args:
        print(f"  {arg}")
    print("krgs:")
    for key, value in krgs.items():
        print(f"  {key}: {value}")
another_function(1, 2, 3, 4, 5, name="Sreenivas", age=25)
another_function("Hello", "World", city="New York", country="USA")
another_function(10, 20)
another_function(10, 20, 30, 40, 50, profession="Engineer")
def yet_another_function(*, a, b, c=10):
    print(f"a: {a}")
    print(f"b: {b}")
    print(f"c: {c}")
yet_another_function(a=1, b=2, c=3)
yet_another_function(a=5, b=10)
# yet_another_function(1, 2, 3)  # this will give an error
