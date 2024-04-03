#13_fibonacci.py

def fib(num):
    fib = []

    for n in range(num):
        if n == 0 or n == 1:
            fib.append(1)
        else:
            fib.append(fib[n-1] + fib[n-2])

    return fib

num = int(input('How many Fibonacci numbers would you like to generate? '))
fib = fib(num)
print(fib)