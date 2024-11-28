# Write a function to find the difference between two lists.

def find_difference(list1, list2):
    return list(set(list1) - set(list2))

print(find_difference([1, 2, 3], [2, 3, 4]))  
