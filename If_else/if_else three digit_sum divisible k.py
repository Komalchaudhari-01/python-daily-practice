
def is_three_digit_and_digit_sum_divisible_by_k(n: int, k: int) -> bool:
    
    if len(str(n)) == 3 and n > 0:
        
        digit_sum = sum(int(d) for d in str(n))
        return digit_sum % k == 0
    
print(is_three_digit_and_digit_sum_divisible_by_k(145,5))