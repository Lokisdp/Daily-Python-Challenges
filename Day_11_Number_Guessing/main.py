import random
from art import logo
print(logo)
print("Welcome to the Number Guessing Game!")
print(f"I'm thinking of a number between 1 and 100.")

result = random.randint(1,100)

def easy(num):
    guess = True
    count = 10
    print(f"You have {count} attempts left.")
    while guess:
        # for i in range(1,11):
        # print(f"You have {count} attempts left.")
        guess_num = int(input("Make a Guess: "))
        if guess_num == result:
            print(f"You got it! the answer is {num}")
            guess = False
        elif guess_num > num:
            count -= 1
            print(f"You have {count} attempts left.")
            print("Too High")
        elif guess_num < num:
            count -= 1
            print(f"You have {count} attempts left.")
            print("Too Low.")

        # if guess_num == result:
        #     print(f"You got it! the answer is {num}")
        #     guess = False
        if count == 0:
            guess = False
            print("You have 0 attempts left.You Lose!!!")

def hard(num):
    guess = True
    count = 5
    print(f"You have {count} attempts left.")
    while guess:
        # for i in range(1,11):
        guess_num = int(input("Make a Guess: "))
        # print(f"You have {count} attempts left.")
        if guess_num == result:
            print(f"You got it! the answer is {num}")
            guess = False
        elif guess_num > num:
            count -= 1
            print(f"You have {count} attempts left.")
            print("Too High")
        elif guess_num < num:
            count -= 1
            print(f"You have {count} attempts left.")
            print("Too Low.")

        # if guess_num == result:
        #     print(f"You got it! the answer is {num}")
        #     guess = False
        if count == 0:
            guess = False
            print("You have 0 attempts left.You Lose!!!")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
if difficulty == "easy":
    easy(result)
elif difficulty == "hard":
    hard(result)
else:
    print("Choose correct level next time. go run it again")



