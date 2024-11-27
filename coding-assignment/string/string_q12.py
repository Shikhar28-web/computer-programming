# Write a function to convert a string to an integer without using built-in functions.

def string_to_int(s):
    num = 0
    sign = 1
    i = 0

    if s[i] == "-":
        sign = -1
        i += 1

    for char in s[i:]:
        num = num * 10 + (ord(char) - ord('0'))

    return sign * num


print(string_to_int("-123"))  
