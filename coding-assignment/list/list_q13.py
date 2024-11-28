# Write a function to remove an element from a list by value.

def remove_element(lst, element):
    if element in lst:
        lst.remove(element)
    return lst

print(remove_element([1, 2, 3, 4, 5], 3)) 