import random

print(
    "The game is simple. I will choose a number from 1 to 100.Your job is to guess the number.Don't worry I will help you :)")
number = random.randrange(1, 100)
you_win = False
total_attempts = 0
while not you_win:
    current_guess = int(input("Please choose a number from 1 to 100: "))
    total_attempts += 1
    if current_guess == number:
        you_win = True
        print(f"Yes! This is the number. You will win the game!Congratulations!You needed {total_attempts} attempts.")
    elif number > current_guess:
        print("No. The number is bigger")
    elif number < current_guess:
        print("No. The number is smaller")
