 # - import certain math functions:
from math import *

# print("Hello world")

# VARIABLES AND DATATYPES -
user_name = "Abdul Rehan"
age = 21
is_user = True

# print(is_user)

# WORKING WITH STRINGS -
# phrase = "This is a car"
# print(phrase[0]) # - grabbing characters from a string
# print(phrase.index("a")) # - gives an index of a char
# print(phrase.replace("car", "cycle"))

# WORKING WITH NUMBERS -
value = 5

# print(str(value) + " is my age") # - convert a number to string
# print(abs(value))
# print(pow(value, 2)) # - value ^ 2
# print(max(value, 2))
# print(min(value, 2))
# print(round(3.5))
# print(floor(3.5)) # - it requires the use of the math library
# print(ceil(3.5)) # - it requires the use of the math library
# print(sqrt(2)) # - it requires the use of the math library

# GET INPUT FROM USER -
# name = input("Enter your name?\n")
# age = input("Enter your age?\n")
# print("Welcome, " +  name + "!")
# print("You are " + age +" years old.")

# BUILD A BASIC CALCULATOR -
# num_one = input("Enter the first value?:\n")
# num_two = input("Enter the second value?:\n")
# result = float(num_one) + float(num_two)
# print(result)

# LISTS -
information = ["Abdul Rehan", 21, "SWE @ AU"]
information[2] = "SDE @ AU"
print(information[-1])
print(information[0])
print(information[1])
print(information[1:])
print(information[0:2])