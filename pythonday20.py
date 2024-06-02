#🐍 Day 20: Crunch Those Numbers: Building a Calculator 🐍
'''
Homework: Your Calculator, Your Rules
Error Handling: What if someone tries to divide by zero or enters an invalid operator? Add checks for these.
More Operators: Extend your calculator to handle other operators like % for modulo.
'''
from pythonday18 import math_functions
def calculate(expressions):
    num1, operator, num2 = expressions.split() # split the expressions into 3 parts
    num1,num2 = float(num1),float(num2) # convert the strings into floats
    if operator == '+':
        return math_functions.add(num1,num2)
    elif operator == '-':
        return math_functions.subtract(num1,num2)
    elif operator == '*':
        return math_functions.multiply(num1,num2)
    elif operator == '/':
        return math_functions.divide(num1,num2)
    elif operator == '%':
        return math_functions.modulo(num1,num2)
    elif operator == '**':
        return math_functions.power(num1,num2)
    elif operator == '//':
        return "syntax error"
    elif num1 == '0':
        return "syntax error"
    else:
        return "Invalid operator"
while True:
        expressions = input("Enter an expression: ")
        if expressions == 'q':
            break
        result = calculate(expressions)
        print(result)