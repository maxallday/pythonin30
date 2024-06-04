#🐍 Day 24: One-Liner Wonders: List Comprehensions 🐍
squares = []
for i in range(1, 6):
    i+=1
    #squares.append(i*i)
    squares = [i * i for i in range(1, 6)]
#print(squares)
'''
Homework: Loop-to-Comprehension Conversion
Convert Loops: Take three of your previous .
Filtering: Create a list of even numbers between 1 and 100 using a list for-loops and convert them to list comprehensionscomprehension.
Nested Comprehension: Try a nested list comprehension if you dare!
'''   
#Convert Loops: Take three of your previous for-loops and convert them to list comprehensions.

squares = []
for i in range(1, 20):
    i+=1
    #squares.append(i*i)
    squares = [i * i for i in range(1, 20)]
    print(squares)

#Filtering: Create a list of even numbers between 1 and 100 using a list for-loops and convert them to list comprehensionscomprehension.
squares = []
for i in range(1, 100):
    i+=1
    if i%2==0:#check if it is even number
       #squares.append(i*i)
        squares = [i * i for i in range(1, 100) if i%2==0]  #
        print(squares)
#Nested Comprehension: Try a nested list comprehension if you dare!
squares = []
for i in range(1, 100):
    i+=1
    if i%2==0:#check if it is even number
        #squares.append(i*i)
        squares = [i * i for i in range(1, 100) if i%2==0 for i in range(1, 100)]  #
        print(squares)