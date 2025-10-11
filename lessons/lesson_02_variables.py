#lets learn abou the variables
# variable = A container for a value(string,integer,float,boolean)
# A variable behaves as if it was the value it contains
# each variable must have a unique name

# = used for assigning a value to variable

# strings
first_name = "Sreenivas"
favorite_food = "biryani"
your_email = "thisisfake@email.com"
print(first_name)

print(f"hello {first_name}")
# f for formatting

#Integers
#make sure there in the quotes
what_is_your_age = 33
how_many_you_need = 33
num_og_pull_requests = 30

print(what_is_your_age)
print(f"we have {num_og_pull_requests}")
print(f"the total number i am looking for is {how_many_you_need}")

# float
# a float will be a number but it has decimals
the_average_numbers_are = 3.1234
what_is_your_gpa = 3.5
how_log_is_the_distance = 2134.3456

print(f"your GPA is {what_is_your_gpa}")
print(f"i know the average {the_average_numbers_are}")
print(f"you ran {how_log_is_the_distance}")

#boolean
#true or false
is_student =True
are_graduate = False
for_sale = True
print(f"are you a student {is_student}")
print(f"are you gradeaute {are_graduate}")

if is_student:
    print(" you a student")
else:
    print("you are not a student")
    
    
if for_sale:
    print( "Yes the item is for sale")
else:
    print(" this not for sale")