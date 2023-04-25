from random import randrange
from time import sleep

print("=" * 40)
print("Welcome to the game!!")
print("=" * 40)
sleep(1)


secret_number = randrange(1, 101)
total_try = 3

for turn in range(1, total_try + 1):
    print(f"try {turn} of {total_try}")
    guess = int(input("What number do you think is between 1 and 100? "))
    print(f"You write {guess}")

    if 1 <= guess <= 100:
        righ = guess == secret_number
        bigger_than = guess > secret_number
        less_than = guess < secret_number

        if (bigger_than):
            sleep(0.5)
            print("You write a number bigger tha the secret number!")
        elif(less_than):
            sleep(0.5)
            print("You write a number less that the secret number!")
        elif(righ):
            sleep(1)
            print("You're right, you write the exaclety number!")

    elif 1 > guess or guess > 100:
        print("You need to write a number between 1 and 100!!")