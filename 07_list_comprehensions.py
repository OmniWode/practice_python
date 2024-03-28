#07_list_comprehensions.py

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

even = [item for item in a if item%2 ==0 ]

print(even)
