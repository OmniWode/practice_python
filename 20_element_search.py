#20_element_search.py

def element_search(num,a):
	if num in a:
		return True
	else:
		return False

def binary_search(num,a):
	print('== DEBUG ==')
	print('searching list:',a)
	print('search query:',num)

	if len(a) == 1:
		if num == a[0]:
			return True
		else:
			return False
	else:
		n = int(len(a)/2)
		if num == a[n]:
			return True
		elif num < a[n]:
			for i in range(n):
				a.pop()
			binary_search(num,a)
		else:
			for i in range(n):
				a.pop(0)
			binary_search(num,a)


def main():
	a = [1, 3, 5, 30, 42, 43, 500]
	print('Given list is:',a)
	num = int(input('Please enter a search query:\n>>> '))

	#in_list = element_search(num,a)
	in_list = binary_search(num,a)

	print('Seach query is in given list:',in_list)

if __name__ == '__main__':
	main()