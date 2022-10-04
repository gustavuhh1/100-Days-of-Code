import random
from secrets import choice

# Rock
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissor = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

choice = int(input("select 0 rock, 1 paper, 2 scissor."))

player_choice = choice

choice = random.randint(0,2)

bot_choice = choice
print(f"Bot choice = {bot_choice}")
if player_choice > 0 or player_choice < 2:
    print("You typed an invalid number, you lose!!")
elif player_choice == 0 and bot_choice == 2:
    print("You win!!")
elif bot_choice == 0 and player_choice == 2:
    print("You lose!!")
elif bot_choice > player_choice:
    print("You lose!!")
elif player_choice > bot_choice:
    print("You win!!")
elif player_choice == bot_choice:
    print("It's a Draw!!")
else:
    print("You type invalid number")