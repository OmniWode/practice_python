#10_list_overlap_comprehensions.py

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

c1 = [item for item in a if item in b]
c2 = []
[c2.append(item) for item in c1 if item not in c2]

print(c2)