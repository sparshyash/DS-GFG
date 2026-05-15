# string slicing
my = "Sparsh Garg"
print(my[2])
print(my[6:8])
#leave end blank
print(my[1:])
print(my[0:5:2])
print(my[::-1])
print(my.split())
bh='hello sparsh'
# title changes first letter to capital
print(bh.title())





# STRING MANIPULATION

name = input("What's your name? ")
if name == "David" or name == "david":
  print("Hello Baldy!")
else: 
  print("What a beautiful head of hair!")

#Right now, if the user writes "DAVID" or "david", the if statement works correctly. However, "DaVID" does not give the correct output.

#To the computer, " david", "dAviD", and "david" are completely different.

# To simplify what the user typed in, we can add these functions to the end of the name of the variable:

# Stringname.lower()
# ----      .upper--
# ----------.title--




# .lower = all letters are lower case
# .upper = all letters are upper case
# .title = capital letter for the first letter of every word
# .capitalize = capital letter for the first letter of only the first word

# Adding .strip() removes any spaces on either side of the word.

# 👉 We can chain these functions together.




