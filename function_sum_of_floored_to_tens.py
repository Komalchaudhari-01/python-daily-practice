''''
Given two integers a and b, return the sum of the two numbers where both numbers are floored 
to the nearest ten.

Flooring to the nearest ten means removing the unit digit and rounding the number down to the 
nearest multiple of 10.

Assume both the numbers are positive integers.'''

def sum_of_floored_to_tens(a:int, b:int):
    a = (a//10) * 10
    b = (b//10) * 10
    return a + b

print(sum_of_floored_to_tens(23, 47))