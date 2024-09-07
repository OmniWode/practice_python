#24_draw_a_board_game.py

def draw_board(size):
	draw_rows(size)
	for n in range(size):
		draw_cols(size)
		draw_rows(size)


def draw_rows(size):
	print(" ---" * size)

def draw_cols(size):
	# change seperator to no space
	print("|   " * size, "|", sep="")

def main():
	size = input("what sized board would you like?\n> ")
	print("here is your game board:\n")
	draw_board(int(size))


if __name__=="__main__":
	main()