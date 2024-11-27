# Write a function to check if a string contains another string without using built-in functions.


def contains_string(s1, s2):
    for i in range(len(s1) - len(s2) + 1):
        if s1[i:i + len(s2)] == s2:
            return True
    return False


print(contains_string("hello", "ell"))  
