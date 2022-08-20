import random

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

# Generate a seed for the random library. This will be generated based on system time since no value is provided.
random.seed()

#Write your code below this line 👇
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))

computer_choice = random.randint(0, 2)

if computer_choice == 0:
    if user_choice == 0:
        print(rock)
        print("Computer chose:")
        print(rock)
        print("Draw")
    elif user_choice == 1:
        print(paper)
        print("Computer chose:")
        print(rock)
        print("You win")
    elif user_choice == 2:
        print(scissors)
        print("Computer chose:")
        print(rock)
        print("You lose")
elif computer_choice == 1:
    if user_choice == 0:
        print(rock)
        print("Computer chose:")
        print(paper)
        print("You lose")
    elif user_choice == 1:
        print(paper)
        print("Computer chose:")
        print(paper)
        print("Draw")
    elif user_choice == 2:
        print(scissors)
        print("Computer chose:")
        print(paper)
        print("You win")
elif computer_choice == 2:
    if user_choice == 0:
        print(rock)
        print("Computer chose:")
        print(scissors)
        print("You win")
    elif user_choice == 1:
        print(paper)
        print("Computer chose:")
        print(scissors)
        print("You lose")
    elif user_choice == 2:
        print(scissors)
        print("Computer chose:")
        print(scissors)
        print("Draw")