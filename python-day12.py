#  🐍 Day 12: Strings Attached: Text Manipulation Techniques 🐍
print("🐍 Day 12 of python safari: Strings Attached: Text Manipulation Techniques 🐍")
# 🚨 Don't change the code below 
print("Hello Lilly!".upper())
#replace(old, new): Replaces all occurrences of the old substring with the new substring.
'''
text = "I like apples"
new_text = text.replace("apples", "bananas")
print(new_text)  # Output: "I like bananas"
'''
text = "Hello Lilly"
print(text.__add__(" and Cindly!")) #add
#Homework: String Exercises
'''Initials: Take a full name from the user and print the initials in uppercase. 
Hint: There's a method for that. You don't have to work hard.
'''
text = input("Enter your full name: ")
initials = text.split(" ")
new_initials = initials[0][0].upper() + initials[1][0].upper()
print(new_initials) 
#print(text[0].upper() + " " + text[0].upper())
#Sentence Reverser: Ask the user for a sentence and print it out in reverse.
# The method for asking the user for more information is input()

input = input("Enter a sentence: ")
print(input[::-1])
