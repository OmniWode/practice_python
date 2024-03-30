#09_guessing_game_01.py

import random

goal = random.randint(1,9)
win = False

print('I\'m thinking of a number between 1 and 9, inclusive.')
print('See if you can guess it!')

while win == False:
    guess = int(input('Your guess : '))

    if guess < goal:
        print('Guess is too low! Try again')
    elif guess > goal:
        print('Guess is too high! Try again')
    else:
        print ('You guessed my number! Well done')
        win = True

print('GAME OVER')