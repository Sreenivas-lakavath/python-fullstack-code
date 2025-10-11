# typecasting = the process of converting a value of one data type to another( string, integer,float,boolean)
# Explicit vs Implicit

name = "sreenivas"
age = 33
gpa = 3.1
student = True
# above are four basic data types

# type(name)
print(type(name))
print(type(age))
print(type(student))

age = float(age)
print(type(age))

gpa = int(gpa)
print(type(gpa))

student = str(student) #built str
print(type(student))

age = bool(age)
print((age))

# all explicit casting is manually chaning value or variate into a different data types by using one of these cast keywords

# Implicit casting is changing the data type can be converted automatically

x = 2
y = 3.0 

x = x/y
print(x) # initially we gave integer but then changed to float -------> General idea