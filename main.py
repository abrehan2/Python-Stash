 # - import certain math functions:
from math import *

# print("Hello world")

# VARIABLES AND DATATYPES -
# user_name = "Abdul Rehan"
# age = 21
# is_user = True

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
# information = ["Abdul Rehan", 21, "SWE @ AU"]
# information[2] = "SDE @ AU"
# print(information[-1])
# print(information[0])
# print(information[1])
# print(information[1:])
# print(information[0:2])

# LISTS FUNCTIONS -
# lucky_numbers = [4,6,8,9,3,2,5,0,11]
# friends = ['Qasim', 'Ali', 'Shahmeer', 'Fatima']
# friends.extend(lucky_numbers) # - the friends list will have all the elements of lucky_numbers list as well
# friends.append("Rehan") # - it adds individual elements at the end of a list
# friends.insert(0, "Najam") # - it adds an individual element in a list
# friends.remove("Fatima") # - it removes an individual element from a list
# friends.clear() # - it removes all the elements from a list
# friends.pop() # - it removes an element from the end of a list
# print(friends.index("Najam")) # - it gives an index of an element from a list
# print(friends.count("Najam")) # - it will tell me how many times the value 'Najam" has come in a list
# friends.sort() # - it sorts a list in the ascending order
# friends.reverse() # - it reverses the order of a list
# friends2 = friends.copy() # - friends2 will have all the same elements of 'friends'
# print(friends2)

# TUPLES -
# IT IS A TYPE OF DATA STRUCTURE THAT CANNOT BE CHANGED OR MODIFIED ONCE CREATED
# coordinates = (4,5)
# print(coordinates[0])

# FUNCTIONS -
# EXAMPLE 1:
# def hello(name, num): print("Hello, " + name + "! with " + str(num))
# hello("Rehan", 26)

# EXAMPLE 2:
# def cube(num):
# return num*num*num
# print(cube(3))

# IF STATEMENTS -
# is_male = True
# is_tall = False
#
# if is_male and is_tall:
#     print("You are a tall male")
#
# elif is_male and not(is_tall):
#     print("You are a short male")
#
# else:
#     print("You are either not male or not tall or both")

# DICTIONARY -
# Keys need to be unique
# month = {
#     "Jan": "January",
#     "Feb": "February",
#     "Mar": "March",
#     1: "EHH"
# }
#
# print(month["Jan"])
# print(month.get("Mar"))
# print(month.get("Dec", "Not a valid key"))
# print(month[1])
# print(month.get(1))

# # WHILE LOOP -
# i = 1
# while i <= 10:
#     print(i)
#     i+= 1
#
# print("DONE WITH LOOP")

# BUILDING A GUESSING GAME -
# secret_word = "Giraffe"
# guess = ""
# guess_count = 0
# guess_limit = 3
# out_of_guesses = False
# 
# while guess != secret_word and not(out_of_guesses):
#     if guess_count < guess_limit:
#         guess = input("Enter guess: ")
#         guess_count += 1
#     else:
#         out_of_guesses = True
# 
# if out_of_guesses:
#     print("Out of guesses, You lose!")
# else: print("You win!")

# FOR LOOP -
# for letter in "Rehan":
#     print(letter)

# food = ["Pizza", "Burger"]
# len(food)
# for f in food:
#     print(f)

# for i in range(10):
#     print(i)

# for i in range(3, 10):
#     print(i)

# food = ["Pizza", "Burger"]
# for i in range(len(food)):
#     print(i, food[i])

# EXPONENT FUNCTION -
# print(2**3) # 2^3
# def raise_to_power(base_num, pow_num):
#     result = 1
#     for i in range(pow_num):
#         result *= base_num
#
#     return result
#
# print(raise_to_power(2, 3))

# 2D LISTS & NESTED LOOPS -
# number_grid = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9],
#     [0]
# ] # 4 - rows & 3 - cols

# print(number_grid[3][0])

# for row in number_grid:
#    for col in row:
#        print(col)

# TRY EXCEPT -
# try:
#    answer = 10/0
#    number = int(input("Enter a number: \n"))
#    print(number)
# except ZeroDivisionError as err:
#     # value = 10/0 - for this types of errors
#     print(err)
# except ValueError:
#     print("Invalid value")

# CLASSES & OBJECTS -
# class Student:
#     def __init__(self, name, age):
#      self.name = name
#      self.age = age
#
# class Person(Student):
#    pass#
#
# student = Student("Ali", 21)
# person = Person("Rehan", 23)#
#
# print(student.name)

# POLYMORPHISM
# class Car:
#   def __init__(self, brand, model):
#     self.brand = brand
#     self.model = model
#
#   def move(self):
#     print("Drive!")
#
# class Boat:
#   def __init__(self, brand, model):
#     self.brand = brand
#     self.model = model
#
#   def move(self):
#     print("Sail!")
#
# class Plane:
#   def __init__(self, brand, model):
#     self.brand = brand
#     self.model = model
#
#   def move(self):
#     print("Fly!")
#
# car1 = Car("Ford", "Mustang")       #Create a Car class
# boat1 = Boat("Ibiza", "Touring 20") #Create a Boat class
# plane1 = Plane("Boeing", "747")     #Create a Plane class
#
# for x in (car1, boat1, plane1):
#   x.move()
