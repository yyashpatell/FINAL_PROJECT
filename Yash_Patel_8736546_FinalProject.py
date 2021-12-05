print("Welcome to the game of ROCK ,PAPERS AND SCISSORS!!!!!. Lets play>>>>>>")
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
#reference for this patterns: https://www.asciiart.eu/people/body-parts/hand-gestures

import random
#used random command which generates random number.

class Player:
    def __init__(self, player_dec):
        self.player_dec = player_dec

    Player_dec = input("\nWhat do you choose? 0 for Rock, 1 for Paper or 2 for Scissors: ")
    if Player_dec == "0":
        print(f"You Choose: Rock \n{rock}")
    elif Player_dec == "1":
        print(f"You Choose: Paper \n{paper}")
    elif Player_dec == "2":
        print(f"You Choose: Scissor \n {scissors}")
    else:
        print("Invalid Number")
    def Computer_dec(self,computer_dec):

        self.computer_dec = computer_dec
    computer_dec = random.randint(0, 2)
# print(Computer_dec)
    if computer_dec == 0:
        print(f"Computer Choose: Rock\n{rock}")
    elif computer_dec == 1:
        print(f"Computer Choose: Paper\n{paper}")
    elif computer_dec == 2:
        print(f"Computer Choose: Scissor\n{scissors}")

    if Player_dec == "0" and Computer_dec == 2:
        print("You Win, WELDONE:)")
    elif Player_dec == "2" and Computer_dec == 1:
        print("You Win, WELDONE:)")
    elif Player_dec == "1" and Computer_dec == 0:
        print("You Win, WELDONE:)")
    elif Player_dec == "0" and Computer_dec == 0:
        print("its a Draw")
    elif Player_dec == "1" and Computer_dec == 1:
        print("its a Draw")
    
