# Write a function to insert an element at a specific position in a list.

def insert_element(lst, index, element):
    lst.insert(index, element)
    return lst

print(insert_element([1, 2, 3, 4, 5], 2, 9)) 