#🐍 Day 13: Modular Magic: Dive Into Functions 🐍
'''
What Are Functions?
A function is a reusable block of code that performs a specific action. 
By using functions, you can write code once and use it multiple times, making your programs more modular and easier to debug.
'''
# 🚨 Don't change the code below 👇

def greet_user(name):
    #print(f"Hello, {name}")
   name= input("Type your name: ")
   print("Hello", name)

greet_user("name")
'''
Homework: Create Your Own Functions
Simple Calculator: Create a function that takes two numbers and an operator (+, -, *, /) as arguments. It should return the result of the operation.
'''
def calc(num1, num2, operator):
    
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        return num1 / num2
    else:
        return "Error"
num1 = float(input("Enter the first number: "))    
num2 = float(input("Enter the second number: "))
operator = input("Enter the operator (+, -, *, /): ")  

result =calc(num1, num2, operator)
print(result)

#String Reverser: Write a function that takes a string as an input and returns it reversed.
def string_reverser():
    text = input("Enter a sentence: ")
    return ''.join(reversed(text))
print(string_reverser())