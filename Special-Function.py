# Special-Function
import turtle
import sys
import random
name = input("Enter your name:")
lastname = input("Enter your lastname:")
job = input("Enter your job:")
def bot(name,lastname,job):
    print("Hi {} {} you are working as {} in one office(maybe)".format(name,lastname,job))
bot(name,lastname,job)

#bored function
tired = input("Are you tired?").lower()
bored = input("Are you bored?").lower()
if tired and bored == "yes" or tired and bored == "y":
    print("Let's play guess game")
    secret = random.randint(1,50)
    guess = input("guess(between 1 to 50):")
    while guess != secret:
        guess = input("guess(between 1 to 50):")
        if guess > secret:
            guess = input("guess(between 1 to 50):")
            print("make a lower guess")
        elif guess < secret:
            print("your guess is low")
        elif guess == secret:
            guesss = input("you won do you want to play again?(y,n):").lower()
        elif guess == "n":
            sys.quit()
if tired == "yes" and bored == "no":
    print("Let's play a other game (lucky game)")
    secret2 = random.randint(1,10)

elif secret2 == 2:
    print("you are not lucky")
elif secret2 == 3:




