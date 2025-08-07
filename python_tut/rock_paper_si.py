import random

option = ("rock","paper","scissors")
player = None
computer = random.choice(option)
player  = input("Enter your choice rock, paper, scissors: ")

print(f"Player:{player}")
print(f"Computer:{computer}")

if player == computer:
        print("you have won the round")
else:
        print("better luck next time!!")