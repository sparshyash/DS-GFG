from getpass import getpass as input

print("E P I C    🪨  📄 ✂    B A T T L E \n")
print("Select your move (R, P or S)\n")


player1Move = input("Player 1 > : \n")

player2Move = input("Player 2 > : \n")


if player1Move=="R":
  if player2Move=="R":
    print("You both picked Rock, draw!")
  elif player2Move=="S":
    print("Player1 smashed Player2's Scissors into dust with their Rock!")
  else:
    print("Player1's Rock is smothered by Player2's Paper!")
elif player1Move=="P":
  if player2Move=="R":
    print("Player2's Rock is smothered by Player1's Paper!")
  elif player2Move=="S":
    print("Player1's Paper is cut into tiny pieces by Player2's Scissors!")

  else:
        print("Two bits of paper flap at each other. Dissapointing. Draw.")
elif player1Move=="S":
            if player2Move=="R":
                print("Player 2's Rock makes metal-dust out of Player1's Scissors")
            elif player2Move=="S":
                print("Ka-Shing! Scissors bounce off each other like a dodgy sword fight! Draw.")
            else:
                print("Player1's Scissors make confetti out of Player2's paper!")
else:
    print("invalid move")