'''
Count Odd 3 Digit Numbers (Ignore None)
Write a function count_odd_three_digit_nums(nums) that takes a list of integers nums and returns the count of numbers that are:

Odd.
Three-digit numbers (ignoring the negative sign if present).
Not None.'''

def count_odd_three_digit_nums(nums):
    count = 0

    for num in nums:
        if num is None:
            continue

        if abs(num) >= 100 and abs(num) <= 999 and num % 2 != 0:
            count += 1

    return count
    

print(count_odd_three_digit_nums([None, 120, 301, -401, 78]))
        
