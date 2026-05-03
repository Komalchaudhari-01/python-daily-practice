
def is_present_in_opposite_halves(elem, l1: list, l2: list):
    """
    Determines whether an element is present in the first half of one list 
    and the second half of the other list, or vice versa.

    Args:
        elem (Any): The element to check for.
        l1 (list): The first list to search.
        l2 (list): The second list to search.

    Returns:
        bool: True if `elem` is present in opposite halves of `l1` and `l2`, 
        False otherwise.
    """
    n1 = len(l1)//2
    n2 = len(l2)//2
    return (elem in l1[:n1] and elem in l2[n2:]) or (elem in l1[n1:] and elem in l2[:n1])

print(is_present_in_opposite_halves(3, [1, 2, 3, 4], [3, 4, 5, 6]))