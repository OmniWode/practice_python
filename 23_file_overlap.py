#23_file_overlap.py

def read_file(file):

	with open(file,'r') as open_file:
		all_text = open_file.read()

	string_list = all_text.split()

	int_list = []

	for string in string_list:
		int_list.append(int(string))

	return int_list

def find_overlap(list1,list2):
	overlap = []

	for item in list1:
		if item in list2:
			overlap.append(item)

	return overlap


def main():
	path = 'files/'
	file1 = path + 'primenumbers.txt'
	file2 = path + 'happynumbers.txt'

	prime_list = read_file(file1)
	happy_list = read_file(file2)

	overlap = find_overlap(prime_list, happy_list)

	print(overlap)


if __name__ == '__main__':
	main()