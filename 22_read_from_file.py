#22_read_from_file.py

def count_names(name_list):
	name_count = {}

	for name in name_list:
		if name in name_count:
			name_count[name] += 1
		else:
			name_count[name] = 1

	return name_count

def count_categories(scene_list):
	category_count = {}

	for scene in scene_list:
		category = scene[3:-26]
		if category in category_count:
			category_count[category] += 1
		else:
			category_count[category] = 1

	return category_count

def main():
	path = 'files/'
	#file = path + 'nameslist.txt'
	file = path + 'categories.txt'

	print(file)

	with open(file,'r') as open_file:
		all_text = open_file.read()

	string_list = all_text.split()

	#name_count = count_names(string_list)
	#print(name_count)


	# extra
	category_count = count_categories(string_list)
	print(category_count)



if __name__ == '__main__':
	main()