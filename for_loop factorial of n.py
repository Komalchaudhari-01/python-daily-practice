
n=int(input("Enter your number"))
factorial=1
for i in range(n,0,-1):
    factorial=factorial*i
print(f"Factorial of {n} is {factorial}")