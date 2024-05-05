#22_read_from_file.py

def count_names(name_list):
	name_count = {}

	for name in name_list:
		if name in name_count:
			name_count[name] += 1
		else:
			name_count[name] = 1

	return name_count

def main():
	path = 'files/'
	file = path + 'nameslist.txt'

	print(file)

	with open(file,'r') as open_file:
		all_text = open_file.read()

	name_list = all_text.split()

	name_count = count_names(name_list)
	print(name_count)

if __name__ == '__main__':
	main()