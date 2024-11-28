# Write a function to remove an element from a list by index.

def remove_element_by_index(lst, index):
    if 0 <= index < len(lst):
        lst.pop(index)
    return lst

print(remove_element_by_index([1, 2, 3, 4, 5], 2))  