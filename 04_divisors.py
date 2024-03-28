#04_divisors

num = int(input("Please enter a number: "))
div = []

for i in range(1,num+1):
    if num%i == 0:
        div.append(i)

print("The list of divisors is: " + str(div))