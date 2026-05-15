# # numbers game 1
# print("You have to enter any no. betwen 1 to 10")
# count = 0
# sum1 = 0
# sum2 = 0
# while True:
#   player1score = int(input("Player 1 score: "))
#   player2score = int(input("Player 2 score: "))
#   sum1+=player1score
#   sum2+=player2score
#   count+=1
#   if (count == 3):
#      break
# print("player1score is", sum1, "and player 2 score is" ,sum2)
# # number facts game 

# print("Welcome to Math Facts Game")
# print()
# print("How well do you know your math facts? Pick a number and I will give you 10 math facts to solve.")
# print()

# fact_family = int(input("Name your multiples: "))
# print()

# counter = 0
# for i in range(1, 11):
#   correct_answer = i*fact_family
#   print(i, "x", fact_family)
#   answer = int(input("> "))
#   if answer == correct_answer:
#     print("You got it right!")
#     counter += 1
#   else:
#     print("That's not correct. It should have been", correct_answer)

# if counter == 10:
#   print("Wow! A perfect score! 🥳")
# else:
#   print("You got", counter, "out of 10 correct.")
#   # Guess the number

# print("Welcome to Guess the Number.\n")

# print("Guess a number between 1 and 10 and I will tell you if you are too low, too high, or get it correct.\n")

# print("Let's play!\n")

# import random
# attempt = 1
# myNumber = random.randint(1,10)

# while True: 
#   user_guess = int(input("Pick a number between 1 and 10: "))
#   if user_guess < myNumber:
#     print("That number is too low. Try again!")
#     attempt += 1
#   elif user_guess > myNumber:
#     print("That number is too high. Try again!")
#     attempt += 1
#     continue
#   elif user_guess == myNumber:
#     print("You are a winner! 🥳🥳")
#     break 
#     exit()
#   else:
#     print("That is not a number I recognize.")
# print("It took you", attempt, "attempt(s) to get the correct answer.")
# #character Game
# import random

# def rollDice(sides):
#   result = random.randint(1,sides)
#   return result

# def roll_6_and_8():
#   roll_6_sided_dice = rollDice(6)
#   roll_8_sided_dice = rollDice(8)
#   health = roll_6_sided_dice * roll_8_sided_dice
#   return health

# print("⚔Character stats generator⚔")
  

# haveACharacter = "yes"

# while haveACharacter == "yes":
#   character = input("Name your warrior: ")
#   health = str(roll_6_and_8())
#   print("Their health is ", health,"hp" ) 
#   haveACharacter = input("Want to create another character?")
#Music Game
# import audio
# import os, time

# def play():
#   source = audio.play_file('audio.wav')
#   source.paused = False # unpause the playback
#   while True:
#     stop_playback = int(input("Press 2 anytime to stop playback and go back to the menu : ")) # giving the user the option to stop playback
#     if stop_playback == 2:
#       source.paused = True # let's pause the file 
#       return # let's go back from this play() subroutine
#     else: 
#       continue
  
# while True:
#   os.system("clear")
#   print("🎵 MyPOD Music Player ")
#   time.sleep(1)
#   print("Press 1 to Play")
#   time.sleep(1)
#   print("Press 2 to Exit")
#   time.sleep(1)
#   print("Press anything else to see the menu again")
#   userInput = int(input())
#   if userInput == 1:
#     print("Playing some proper tunes!")
#     play()
#   elif userInput == 2:
#     exit()
#   else :
#     continue


# import random, os, time

# def rollDice(side):
#   result = random.randint(1,side)
#   return result

# def health():
#   healthStat = ((rollDice(6)*rollDice(12))/2)+10
#   return healthStat

# def strength():
#   strengthStat = ((rollDice(6)*rollDice(8))/2)+12
#   return strengthStat

# while True:
#   print("⚔ CHARACTER BUILDER ⚔")
#   print()
#   name = input("Name your Legend:\n")
#   type = input("Character Type (Human, Elf, Wizard, Orc):\n")
#   print()
#   print(name)
#   print("HEALTH:", health())
#   print("STRENGTH:", strength())
#   print()
#   print("May your name go down in Legend…")
#   print()
#   again = input("Again?:\n")
#   if again=="No" or again=="no":
#     break
#   time.sleep(1)
#   os.system("clear")





