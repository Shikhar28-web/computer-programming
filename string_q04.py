# Write a function to validate if a given string can be interpreted as a decimal number.


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

print(is_number("123.45"))  
print(is_number("abc"))     
