name = input("Enter your name: ")
print("Hello,", name, "! Welcome!")

# Python's input() function is used to take user input. By default, it returns the user input in form of a string. 

print("Hello, World!")

# Printing Variables 

s = "Brad"
print(s)

s = "Anjelina"
age = 25
city = "New York"
print(s, age, city)

x, y = input("Enter two numbers: ").split()
print(x , y)

i = int(input("How old are you?: "))
f = float(input("Evaluate 7/2: "))
print(i, f)

# var

# Variables are used to store data that can be referenced and manipulated during program execution. A variable is essentially a name that is assigned to a value.

#Unlike Java and many other languages, Python variables do not require explicit declaration of type.
 # Type of the variable is inferred based on the value assigned.



x = 5
name = "Alex"  
print(x)
print(name)


# 2. Dynamic Typing: Python is dynamically typed, so the same variable can store different data types
# during execution.


x = 10
x = "Now a string"


# 3. Assigning Same Value: same value can be assigned to multiple variables in a single line.





a = b = c = 100
print(a, b, c)

# del keyword is used to delete a variable from memory. After deletion, the variable can no longer be accessed.



x = 10
del x
print(x)

# 1. Swapping Two Variables: Using multiple assignments, we can swap the values of two variables without needing a temporary variable.

a, b = 5, 10
a, b = b, a
print(a, b)

# 2. Counting Characters in a String: Assign the results of multiple operations on a string to variables in one line.

word = "Python"
length = len(word)
print("Length of the word:", length)


# Keywords 

import keyword
print("The list of keywords are : ")
print(keyword.kwlist)

# Let's categorize all keywords based on context for a more clear understanding.

# Category	Keywords
# Value Keywords

# True, False, None

# Operator Keywords	and, or, not, is, in
# Control Flow Keywords

# if, else, elif, for, while, break, continue, pass, try, except, finally, raise, assert

# Function and Class	def, return, lambda, yield, class
# Context Management	with, as
# Import and Module	import, from
# Scope and Namespace	global, nonlocal
# Async Programming	async, await
# Keywords vs Identifiers
# Keywords	Identifiers
# Reserved words in Python that have a specific meaning.	Names given to variables, functions, classes, etc.
# Cannot be used as variable names.	Can be used as variable names if not a keyword.
# Examples: if, else, for, while	Examples: x, number, sum, result
# Part of the Python syntax.	User-defined, meaningful names in the code.
# They cannot be redefined or changed.	Can be defined and redefined by the programmer.
# Variables vs Keywords
# Variables	Keywords
# Used to store data.	Reserved words with predefined meanings in Python.
# Can be created, modified, and deleted by the programmer.	Cannot be modified or used as variable names.
# Examples: x, age, name	Examples: if, while, for
# Hold values that are manipulated in the program.	Used to define the structure of Python code.
# Variable names must follow naming rules but are otherwise flexible.	Fixed by Python language and cannot be altered.

# ctrl + / for multi comments 

