#18_cows_and_bulls.py

import random

def make_guess(guess, goal):
	correct = False

	if guess == goal:
		correct = True
	else:
		# cows and bulls message here
		print('try again!')
		
		cows = check_cows(guess, goal)
		bulls = check_bulls(guess, goal)

		print(cows,'cows,',bulls,'bulls')


	return correct

def check_cows(guess, goal):
	cows = 0

	for i in range(4):
		if guess[i] == goal[i]:
			cows += 1

	return cows

def check_bulls(guess, goal):
	bulls = 0

	for i in range(4):
		if guess[i] in goal:
			bulls += 1

	return bulls

if __name__=="__main__":
	goal = str(random.randint(1000,9999))
	correct_guess = False
	guess_count = 0


	print('== D E B U G ==')
	print('goal = ',goal)
	print('== D E B U G ==')

	while not correct_guess:
		guess = input('Enter a number:\n>>> ')
		correct_guess = make_guess(guess, goal)
		guess_count += 1
		
	print('Well done! It took you',guess_count,'guesses to find the number')
