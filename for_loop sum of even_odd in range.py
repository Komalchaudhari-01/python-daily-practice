
n = int(input("Enter your number"))
sum_of_even =0
sum_of_odd =0
for i in range(n):
    if i % 2 ==0:
        sum_of_even= sum_of_even+i
    else:
        sum_of_odd = sum_of_odd+i
print(f"Sum of odd is {sum_of_odd}")
print(f"sum of even is {sum_of_even}")
      