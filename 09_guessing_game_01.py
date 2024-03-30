#09_guessing_game_01.py

import random

goal = random.randint(1,9)
win = False

print('I\'m thinking of a number between 1 and 9, inclusive.')
print('See if you can guess it!')

#extra 1
print('Game will continue until you type "exit"')

#extra 2
guess_count = 0

while win == False:
    guess = input('Your guess : ')

    if guess == 'exit':
        win = True
    elif (guess.isdigit()):
        if int(guess) < goal:
            guess_count += 1
            print('Guess is too low! Try again')
        elif int(guess) > goal:
            guess_count += 1
            print('Guess is too high! Try again')
        elif int(guess) == goal:
            #extra 2
            guess_count += 1
            print (f'You guessed my number! Well done, it took you {guess_count} tries to guess')
            print('Let\'s play again! I\'ll think of a new number and reset the guess count...')
            print('Ready!')

            goal = random.randint(1,9)
            guess_count = 0
    else:
        print('Invalid input, please try again')


print('GAME OVER')