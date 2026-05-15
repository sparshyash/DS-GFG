#\lists\\ Lists are mutable in python and takes more memory than tuples 
My=[1,"Hello",'a']
My.append("Hi")# Add element to first
print(len(My))
My.remove("Hello")
My.pop()# Remove first element
My[1]= 'c'
print(My)
#dictionaies
days={"1":"Mon","2":"Tue","3":"Wed"}
print(days["1"])
days["4"]="Thu"
# days.update{"5": "SUn"}
days.pop("1")
#Type casting
age=int(input("enter your age:"))
print(age)
timetable = ["Computer Science", "Math", "English", "Art", "Watch TV"]
# For loop with lists
for lesson in timetable:
  print(lesson)
#Dynamic Lists
list=[]
list.append("Hello")
list.append('m')
list.remove('m')
print(list)
import random
greetings = ["Hello there!", "Konnichiwa", "Guten Tag!", "Bore Da!"]
index = random.randint(0,3)
print(greetings[index])

# This is a simple program that creates a list with a simple subroutine. In the while True loop, the user is adding something to the list. (This is nowhere near as complicated as what you have done).

# 👉 What happens when you run this code and add 'phone' and 'Phone' to your list? Does it create duplicates?
myList = []

def printList():
  print()
  for i in myList:
    print(i)
  print()
j=5
while j>0:
  addItem = input("Item > ") 
  if addItem not in myList:
    myList.append(addItem) 
  
  printList()
  j-=1

#  Here is an easier way to ensure you do not have duplicates. Use these various string manipulations in your loop:

# Note: Whatever you do after the . will happen to the string. If you use .lower, then the string will print in lower case.


# rolodex = []

# def printList():
#   print()
#   for name in rolodex:
#     print(name)
#   print()
# while True:
#   lastName = input("Last Name: ").strip().capitalize()
#   name = f"{firstName} {lastName}"
#   if name not in rolodex:
#     rolodex.append(name)
#   else:
#     print("ERROR: Duplicate name")
# printList()