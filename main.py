import random

def guess(x):
    random_number = random.randint(1,x)
    guess_number = 0
    while guess_number!= random_number:
        guess_number = int(input(f"Guess the number between 1 and {x}: "))
        if guess_number < random_number:
            print('Sorry, guess again. Too low.')
        elif guess_number > random_number:
            print('Sorry, guess again, too high.')
    print('Great! you have guessed the number!')
        
guess(5)
