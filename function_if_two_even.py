'''
Check If Even Two-Digit Number
Write a function is_even_two_digit_number that checks whether a given number is
 an even two-digit number.
A number is considered a two-digit number if it has exactly two digits excluding any negative sign.'''

def is_even_two_digit_number(num):
    if 10 <= abs(num) <= 99 and abs(num)%2 == 0:
        return True
    
print(is_even_two_digit_number(24))