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
        
guess(10)

def computer_guess(x):
    low = 1
    high = x
    feedback =''
    
    while feedback !='c':
        
        if low!=high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f"Is {guess} too high (H), too low (L), or correct (C)??").lower()
        if feedback == 'h':
            high = guess -1
        elif feedback == 'l':
            low = guess +1
    print(f'Yay! The computer has guessed your number {guess}, correctly!')
    
computer_guess(10)
