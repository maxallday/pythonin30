#🐍 Day 19: Package Deal: Importing in Python 🐍
'''
What are Packages?
If a module is like a book, then a package is the bookshelf.
A package is a way of organizing related modules into a single directory hierarchy.

Homework: Your First Package
Math & Utilities Package: Create a package that combines your math and utility modules from yesterday.
Daily Planner: Create a package that has modules for tasks, reminders, and events.
'''
from my_package import math_functions
from pythonday18 import add, subtract, multiply, divide                  
print(math_functions.add(5, 3))
print(subtract(5, 3))
print(add(5, 3))
print(multiply(5, 3))
print(divide(round(5.5), 3))

