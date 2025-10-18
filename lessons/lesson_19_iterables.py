# Copyright (c) 2025 Sreenivas-lakavath
# All rights reserved.

# Iterables lesson
# Iterables are objects that can be looped over
# Examples of iterables: strings, lists, tuples, dictionaries, sets
# Non-iterables: int, float, bool
# We can use the built-in function 'iter()' to get an iterator from an iterable

name = "sreenivas"
for letter in name:
    print(letter)
# here string is an iterable and we are looping through each letter in the string
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    print(number)
# here list is an iterable and we are looping through each number in the list
# using iter() function
name_iterator = iter(name)
print(next(name_iterator))  # s
print(next(name_iterator))  # r
print(next(name_iterator))  # e
# we can use next() function to get the next item from the iterator
numbers_iterator = iter(numbers)
print(next(numbers_iterator))  # 1
print(next(numbers_iterator))  # 2
print(next(numbers_iterator))  # 3
# we can use next() function to get the next item from the iterator
# we can also use a while loop to iterate through an iterable using iter() and next()
name_iterator = iter(name)
while True:
    try:
        letter = next(name_iterator)
        print(letter)
    except StopIteration:
        break   
# here we are using a while loop to iterate through each letter in the string
# until we reach the end of the iterator and get a StopIteration exception
numbers_iterator = iter(numbers)
while True:
    try:
        number = next(numbers_iterator)
        print(number)
    except StopIteration:
        break
# here we are using a while loop to iterate through each number in the list
# until we reach the end of the iterator and get a StopIteration exception
# we can also create our own iterable objects by defining the __iter__() and __next__() methods
class MyIterable:
    def __init__(self, limit):
        self.limit = limit
        self.current = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.current < self.limit:
            number = self.current
            self.current += 1
            return number
        else:
            raise StopIteration
my_iterable = MyIterable(5)
for number in my_iterable:
    print(number)
# here we created our own iterable object that generates numbers from 0 to limit-1
# and we are looping through each number in the iterable
my_iterable_iterator = iter(MyIterable(3))
print(next(my_iterable_iterator))  # 0
print(next(my_iterable_iterator))  # 1
print(next(my_iterable_iterator))  # 2
# we can use next() function to get the next item from our custom iterable iterator
# trying to get next item will raise StopIteration exception
try:
    print(next(my_iterable_iterator))  # raises StopIteration
except StopIteration:
    print("Reached the end of the iterable")
# here we are trying to get the next item from our custom iterable iterator
# and catching the StopIteration exception when we reach the end of the iterable