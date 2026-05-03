'''
Number with More Unique Digits
Given two integers n1 and n2, return the number that contains more unique digits.

If both numbers have the same number of unique digits, return the both as a tuple as (n1, n2).

Assume both the integers n1 and n2 are positive integer.

Hint: Use set to find the unique digits, as sets automatically eliminate duplicates.'''
def number_with_more_unique_digits(n1:int, n2:int):
    n1 = len(set(str(n1)))
    n2 = len(set(str(n2)))
    if n1 > n2:
        return n1
    elif n1 == n2:
        return tuple(n1,n2)
    else:
        return n2
    
print(number_with_more_unique_digits(123, 1122))