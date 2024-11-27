# Write a Python function to check if a given element exists in a tuple.


def element_exists(t, element):
    return element in t

my_tuple = (1, 2, 3)
print(element_exists(my_tuple, 2))  
