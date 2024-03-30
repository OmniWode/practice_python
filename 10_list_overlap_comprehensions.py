#10_list_overlap_comprehensions.py
import random

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

c1 = [item for item in a if item in b]
c2 = []
[c2.append(item) for item in c1 if item not in c2]

print('Base solution')
print('a = ',a)
print('b = ',b)
print('shared = ',c2)

# extra
x_len = random.randint(5,15)
y_len = random.randint(5,15)

x = random.sample(range(30),x_len)
y = random.sample(range(30),y_len)

z1 = [item for item in x if item in y]
z2 = []
[z2.append(item) for item in z1 if item not in z2]

print('Extra solution (random lists)')
print('x = ',x)
print('y = ',y)
print('shared = ',z2)