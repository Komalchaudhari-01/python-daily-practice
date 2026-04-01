
n = int(input("Enter your number"))
x = n
rev = 0
while n > 0:
    a = n % 10
    rev = (rev * 10) + a 
    n = n // 10
if rev == x:
    print(f"{x} is an pallindromic number")
else:
    print(f"{x} is not an pallindromic number")