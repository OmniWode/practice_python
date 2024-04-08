#16_password_generator.py
import random

def generate_password(len,chars):
	password = []

	for i in range(len):
		# choose a random type of char
		# then pick random of that type
		password.append(random.choice(random.choice(chars)))

	password_string = ''.join(password)

	return password_string


def main():

	lower = ['a','b','c','d','e','f','g','h','i','j','k','l',
	'm','n','o','p','q','r','s','t','u','v','w','x','y','z']
	upper = ['A','B','C','D','E','F','G','H','I','J','K','L',
	'M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
	number = ['0','1','2','3','4','5','6','7','8','9']
	symbol = ['?','!','@','#','$','%','^','&','*']

	chars = [lower,upper,number,symbol]

	len = random.randint(8,16)
	password = generate_password(len,chars)
	print(password)


if __name__=='__main__':
	main()