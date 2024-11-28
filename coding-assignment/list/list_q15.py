# Write a function to find the index of an element in a list.

def find_index(lst, element):
    return lst.index(element) if element in lst else -1

print(find_index([1, 2, 3, 4, 5], 3))  