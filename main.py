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

# Write your code below this line 👇
choices = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors"))
print(choices[user_choice])
print("Computer chose: ")
computer_choice = random.randint(0, len(choices) - 1)
print(choices[computer_choice])

if user_choice == computer_choice:
    print("It is a draw")
else:
    if user_choice == 0:
        if computer_choice == 1:
            print("You lose")
        else:
            print("You win")
    elif user_choice == 1:
        if computer_choice == 0:
            print("You win")
        else:
            print("You lose")
    elif user_choice == 2:
        if computer_choice == 0:
            print("You lose")
        else:
            print("You win")

