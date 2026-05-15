print("Hello Bhaiyo")
name=input("What's Your name is :")
print("hlo",name)
#sep 
print("Hello", "World", "Python", sep="-")
# Output: Hello-World-Python
print("Hello", "World", sep=", ", end="!\n")
# Output: Hello, World!
words = ["Python", "is", "awesome"]
print(" ".join(words))
# Output: Python is awesome
#type
a=20
print(type(a))
#Octal
g=0o12
print(g)
#Hexadecimal
g=0x20
print(g)
print(5==3)

#print("\033[?25l",end="")
print("Hello",name)
#Concating
print("Hllo",name,"Do you want tea")
# Adding colour to code
#default=0
#black=30;red=31;green=32;yellow=33blue=34;purple=35;cyan=36;white=37
#Bold-1,underline-2,negative-3,positive-4
print("\033[31m",name,"\033[34m","what's your hobbies")

print("\033[31m",name,"\033[1m","what's your hobbies","\033[0m")
