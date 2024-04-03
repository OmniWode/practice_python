#14_list_remove_duplicates.py

def remove_duplicates(list):
    unique = []

    for item in list:
        if item not in unique:
            unique.append(item)

    return unique


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89,
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

print('full list: ', a)

unique_loop = remove_duplicates(a)
print('loop solution: ',unique_loop)

# extra 
unique_set = set(a)
print('set solution: ',unique_set)