from random import randrange
from time import sleep

def adivinhacao():
    points = 1000
    print("=" * 40)
    print("Welcome to the game!!")
    print(f"You'll starting with {points} of score, and you'll lose your points equal the difference between your choice and the secret!")
    print("=" * 40)
    sleep(1)


    secret_number = randrange(1, 101)
    total_try = 3

    print(secret_number)
    for turn in range(1, total_try + 1):
        print(f"try {turn} of {total_try}")
        guess = int(input("What number do you think is between 1 and 100? "))
        print(f"You write {guess}")
        

        if 1 <= guess <= 100:
            righ = guess == secret_number
            bigger_than = guess > secret_number
            less_than = guess < secret_number

            if(righ):
                sleep(1)
                print("You're right, you write the exaclety number!")
                break
            else:
                if (bigger_than):
                    sleep(1)
                    print("You wrote a number bigger than the secret number!")
                
                elif(less_than):
                    sleep(1)
                    print("You wrote a number less than the secret number!")
                points = points - abs(secret_number - guess)

        elif 1 > guess or guess > 100:
            print("You need to write a number between 1 and 100!!")
        
    print(f"You have {points} points.")