
l =[20,90,-40,80,-19,70,-30]
l1=[]
l2=[]

for i in l:
    if i > 0:
        l1.append(i)
    else:
        l2.append(i)
newlist = l1+l2
print(newlist)