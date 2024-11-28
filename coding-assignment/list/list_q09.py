# Write a function to find the difference between two lists.


def list_difference(lst1, lst2):
    return list(set(lst1) - set(lst2))

print(list_difference([1, 2, 3], [2, 3, 4]))  