#25_guessing_game_02.py

def guess(guess_min, guess_max):
	#picks the median between guess_min and guess_max
	return int((guess_max - guess_min) / 2) + guess_min

def main():
	win = False
	num = 0
	guess_min = 0
	guess_max = 100
	feedback = ""

	compare = ""

	while(not win):
		num = guess(guess_min, guess_max)

		print("my guess is:",num)
		feedback = input("how did i do? ('0'=low, '1'=high, '2'=equal)\n> ")
		
		if(feedback == "0"):
			guess_min = num
		elif (feedback == "1"):
			guess_max = num
		elif (feedback == "2"):
			print("i guessed the right number!")
			win = True
		else:
			print("oops, i don't understand your input!")


if __name__=="__main__":
	main()