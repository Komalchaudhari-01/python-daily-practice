
l = [12,13,16,19,17,20]
largest = l[0]
second = l[0]
lar_in = 0
sec_in = 0
for i in range(len(l)):
    if l[i] > largest:
        second = largest 
        sec_in = lar_in
        largest = l[i]
        lar_in = i
    elif l[i] > second:
        second = l[i]
        sec_in = i


print(f"{second} is second largest element at {sec_in} index number")
print(f"{largest} is largest element at {lar_in} at index number")
