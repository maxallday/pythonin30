#🐍 Day 17: Object-Oriented Python: Introduction to Classes 🐍
#  🚨 Don't change the code below 👇

class Dog:
    def __init__(self, name, breed, color):
        self.name = name
        self.breed = breed
        self.color = color

    def describe(self):
        print(f"My dog's name is {self.name}, breed {self.breed}, and color {self.color}. Woof!")

my_dog = Dog("Joie", "Pug", "brown")
my_dog.describe()
#Homework: Be the Architect
#Create a class called "Person" that has attributes "f_name" and "l_name".
class Person:
    def __init__(self, f_name, l_name, l_age, l_status):
        self.f_name = f_name
        self.l_name = l_name
        self.l_age = l_age
        self.l_status = l_status

    def print_name(self):
        print(f"{self.f_name} {self.l_name}")
my_bio = Person("John", "Doe", 25, "Married to the Streets!!!!")
my_bio.print_name()
#Animal Kingdom: Design a Zoo class that 
#can contain different types of animals with varying attributes.
#Create a class called "Animal".
class Animal:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age
    def __str__(self):
        print(f"{self.name} is a {self.species} and is {self.age} years old.")
   
animal = Animal("Lion", "brown", "3 years") 
animal.__str__()   