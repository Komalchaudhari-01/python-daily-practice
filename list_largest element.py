'''l=[49,38,93,20,48,28,209]
largest = l[0]
for i in range(len(l)):
    if l[i] > largest: 
        largest = l[i]
        index = i
print(f"{largest} is largest element")'''

l=[49,38,93,20,48,28,209]
largest = l[0]

for i,val in enumerate(l):
    if val > largest:
        largest = val
        index = i
print(f"{largest} is largest element at index {index}")