#12_list_ends.py

def list_ends(full_list):
    short_list = []

    short_list.append(full_list[0])
    short_list.append(full_list[len(full_list)-1])

    return short_list

# exercise sample
a = [5, 10, 15, 20, 25]
ends = list_ends(a)
print('The full list is:',a)
print('The end elements are:',ends)