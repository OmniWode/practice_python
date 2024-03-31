#check primality functions

def check_divisor(a,b):
    if a%b == 0:
        return True
    else:
        return False
    
def check_prime(num):
    if num == 1:
        return False

    prime = True

    for i in range(2, num):
        if check_divisor(num,i):
            prime = False

    return prime

num = int(input('Please provide a number to test for primality: '))

if check_prime(num) == True:
    print(str(num),'is a prime!')
else:
    print(str(num),'is not a prime!')

# testing by checking for primes between 1 and 100 (should be 25 total)
primes = []
for n in range(1,100):
    if check_prime(n):
        primes.append(n)

print('The primes between 1 and 100 are:',primes)
print('In total there are',len(primes),'primes bewteen 1 and 100')