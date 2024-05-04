#21_write_to_a_file.py

def make_text(num):
	string = ''
	a = []

	for n in range(num):
		a.append(str(n)+' ')

	string = ''.join(a)

	return string

def save_to_file(file,string):
	with open(file,'w') as open_file:
		open_file.write(string)

def main():
	#extra
	path = 'output_files/'
	file = path+input('Name of output file:\n>>> ')

	num = 10
	
	string = make_text(num)
	save_to_file(file,string)

if __name__ == '__main__':
	main()