
def remove_second_and_second_last(s: str) -> str:
    if len(s) < 4:
        return s
    
    l = list(s)
    del l[1]
    del l[-2]
    
    return "".join(l)

