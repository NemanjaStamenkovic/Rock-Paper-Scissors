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
import random

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))

images = [rock, paper, scissors]

if choice >= 3:
    print("Invalid number You Loose")
else:
    print("You Choose")
    print(images[choice])
    
    randomNum = random.randint(0, 2)
    
    print("Computer Choose")
    print(images[randomNum])
    
    
    if choice == 0 and randNum == 2:
        print("You Win")
    elif randomNum == 0 and choice == 2:
        print("You Loose")
    elif choice == randomNum:
        print("Its A Draw")
    elif choice > randomNum:
        print("You Win")
    elif randomNum > choice:
        print("You Loose")