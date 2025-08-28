
import random as rd
import pyfiglet as pg
art = pg.figlet_format("YOU LOSE 😹")
num = rd.randint(1, 10)
guess = 0
while True:
    try:
        number_guess = int(input("Guess a number between 1 and 10: "))
        guess += 1
        print(f"You've tried to guess {guess}/5")
        if number_guess > num:
            print("Too high, try again!")
        elif number_guess < num:
            print("Too low, try again!")
        if guess == 5:
            print(f"\n\nYou have run out of guessing attempts, the secret number isssssssssssss = {num}")
            print(art)
            break
        elif number_guess == num:
            print("You Guessed it ")
            break
    except ValueError:
        print("Invalid Input, Please enter a number")