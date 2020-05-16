#Guess game
secret_number = "Mohammad"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False
while guess != secret_number and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        out_of_guesses = True
if out_of_guesses:
    print("Game Over")
else:
    print("You Won the game")
        