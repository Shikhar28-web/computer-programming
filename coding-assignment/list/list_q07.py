# Write a function to find the symmetric difference between two lists.

def symmetric_difference(lst1, lst2):
    return list(set(lst1) ^ set(lst2))

print(symmetric_difference([1, 2, 3], [2, 3, 4]))  