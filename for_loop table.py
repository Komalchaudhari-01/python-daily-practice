#direct multiples
'''n=int(input("which table you want?"))
for i in range(n,(n*10)+1,n):
    print(i)'''

n=int(input("which table you want?"))
for i in range(1,11,1):
    print(f"{n}*{i}={n*i}")