

a = input().strip()
b = input().strip()


set1 = set(a)
set2 = set(b)


common = set1 & set2


print(len(common))