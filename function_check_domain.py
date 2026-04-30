'''
Check If the given domain is .com or .in
Write a function is_dot_com_or_dot_in(domain) that takes a string domain 
and checks whether it ends with .com or .in.
The function should return True if the domain has the specified suffix;otherwise, it should return False.'''

def is_dot_com_or_dot_in(domain):
    if domain.endswith(".com") or domain.endswith(".in"):
        return True
    else:
        return False
    
print(is_dot_com_or_dot_in("example.com"))
print(is_dot_com_or_dot_in("mydomain.org"))