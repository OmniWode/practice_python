#15_reverse_word_order.py

def rev_word(sentence):
    temp = sentence.split()
    temp.reverse()
    return ' '.join(temp)

print('Please enter a phrase with mlutiple words:')
string = input('>>> ')
reverse_string = rev_word(string)
print(reverse_string)