# Copyright (c) 2025 Sreenivas-lakavath
# All rights reserved.
# Dictonaries in python

# dictonary is a collection of key value pairs
# key must be unique
# key must be immutable (string,number or tuple)
# value can be anything (mutable or immutable)

my_dictonary = {
    "name": "Sreenivas",
    "age": 24,
    "city": "Hyderabad",
    "is_married": False,
    "hobbies": ["reading", "coding", "gaming"],
    "address": {
        "street": "123 main st",
        "city": "Hyderabad",
        "state": "TS"
    }
}
print(my_dictonary)
print(type(my_dictonary))
print(my_dictonary["name"])
print(my_dictonary["hobbies"])
print(my_dictonary["address"]["city"])  # nested dictonary
print(len(my_dictonary))
my_dictonary["age"] = 25  # update value
print(my_dictonary)
my_dictonary["phone"] = "123-456-7890"  # add new key value pair
print(my_dictonary)
del my_dictonary["is_married"]  # delete key value pair
print(my_dictonary)
# my_dictonary.clear() # clear the dictonary
# print(my_dictonary)
# del my_dictonary # delete the dictonary
# print(my_dictonary) # this will give error
print(my_dictonary.keys())  # get all keys
print(my_dictonary.values())  # get all values
print(my_dictonary.items())  # get all key value pairs
if "name" in my_dictonary:
    print("name is present")
else:
    print("name is not present")
for key in my_dictonary:
    print(key)  # print all keys
for value in my_dictonary.values():
    print(value)  # print all values
for key, value in my_dictonary.items():
    print(f"{key}: {value}")  # print all key value pairs
my_dictonary2 = my_dictonary.copy()  # copy dictonary
print(my_dictonary2)
my_dictonary3 = dict(my_dictonary)  # another way to copy dictonary
print(my_dictonary3)
my_dictonary4 = dict(name="John", age=30, city="New York")  # another way to create dictonary
print(my_dictonary4)

# nested dictonary
users = {
    "user1": {
        "name": "Sreenivas",
        "age": 24,
        "city": "Hyderabad"
    },
    "user2": {
        "name": "John",
        "age": 30,
        "city": "New York"
    },
    "user3": {
        "name": "Jane",
        "age": 25,
        "city": "London"
    }
}
print(users)
print(users["user1"]["name"])
print(users["user2"]["age"])
print(users["user3"]["city"])
for user, info in users.items():
    print(f"{user}:")
    for key, value in info.items():
        print(f"  {key}: {value}")  # nested loop to print nested dictonary
        
# dictonary methods
print(my_dictonary.get("name"))  # get value by key
print(my_dictonary.get("phone", "not found"))  # get value by key
print(my_dictonary.pop("age"))  # remove key value pair and return value
print(my_dictonary)
print(my_dictonary.popitem())  # remove last key value pair and return it
print(my_dictonary)
my_dictonary.update({"age": 26})  # update value
print(my_dictonary)
my_dictonary.update({"phone": "987-654-3210"})  # add new key value pair
print(my_dictonary)
