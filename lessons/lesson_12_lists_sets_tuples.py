# Copyrights (c) 2025 Sreenivas-lakavath
# All rights reserved.
# lists = ordered, mutable, allows duplicate elements
# sets = unordered, mutable, no duplicate elements
# tuples = ordered, immutable, allows duplicate elements

#indexing and slicing works the same for lists and tuples as strings

#lists
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
print(friends)
print(friends[0])
print(friends[1:])
print(friends[-1])
print(friends[1:4]) # 4 is exclusive
friends[1] = "Mike" #muttable
print(friends)
for friend in friends:
    print(friend)
if "Oscar" in friends:
    print("Oscar is a friend")
else:
    print("Oscar is not a friend")
friends.append("Creed") # add to the end of the list
print(friends)
friends.insert(1, "Kelly") # insert at a specific index
print(friends)
friends.remove("Jim") # remove by value
print(friends)
friends.pop() # remove last item
print(friends)
friends.pop(1) # remove item at specific index
print(friends)
friends.sort() # sort the list permanently
print(friends)
friends.reverse() # reverse the list permanently
print(friends)
friends2 = friends.copy() # copy the list
print(friends2)
friends.clear() # clear the list
print(friends)
#tuples
coordinates = (4, 5) # immutable
print(coordinates[0])
print(coordinates[1])
#coordinates[0] = 10 # this will give an error
for coordinate in coordinates:
    print(coordinate)
if 5 in coordinates:
    print("5 is in the coordinates")
#sets
# unordered, unindexed, no duplicate values
utensils = {"fork", "spoon", "knife"}
print(utensils)
for utensil in utensils:
    print(utensil)
if "fork" in utensils:
    print("fork is in the utensils")
else:
    print("fork is not in the utensils")
utensils.add("napkin") # add item to set
print(utensils)
utensils.remove("fork") # remove item from set, gives error if item not found
print(utensils)
utensils.discard("fork") # remove item from set, does not give error if item not found
print(utensils)
utensils.clear() # clear the set
print(utensils)
dishes = {"bowl", "plate", "cup", "knife"}
print(dishes)
utensils = utensils.union(dishes) # join two sets
print(utensils)
dinner_table = utensils.union(dishes) # join two sets
print(dinner_table)
print(len(dinner_table)) # length of set
dinner_table = dinner_table.union(friends2) # join set and list
print(dinner_table)
print(len(dinner_table)) # length of set
dinner_table = dinner_table.union(coordinates) # join set and tuple
print(dinner_table)
print(len(dinner_table)) # length of set