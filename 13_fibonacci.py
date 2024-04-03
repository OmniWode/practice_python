#13_fibonacci.py

def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        num = fib(n - 1) + fib(n - 2)
        return num

def make_list(count):
    fib_list = []

    for a in range(count):
        fib_list.append(fib(a+1))

    return fib_list    

n = int(input('How many Fibonacci numbers would you like to generate? '))
fib_list = make_list(n)
print(fib_list)