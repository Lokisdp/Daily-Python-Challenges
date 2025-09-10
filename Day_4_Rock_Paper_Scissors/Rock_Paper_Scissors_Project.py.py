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

# random_num = random.randint(0,2)
game_list = [rock,paper,scissors]
game_images = ["rock","paper","scissors"]
# random_choice = game_list[random_num]
Choose_num = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
# random_choice = random.choice(game_list)
if Choose_num >= 0 and Choose_num <= 2:
    print(game_list[Choose_num])

random_num = random.randint(0,2)

print(f"Computer choose: {game_images[random_num]}")
print(game_list[random_num])


if Choose_num >= 3 or random_num < 0:
    print("You typed an invalid number. you lose!")
elif Choose_num == 0 and random_num == 2:
    print("you Win")
elif random_num == 0 and Choose_num == 2:
    print("You Lose")
elif random_num > Choose_num:
    print("You Lose!")
elif Choose_num > random_num:
    print("you Win!")
elif Choose_num == random_num:
    print("It's a Draw!")