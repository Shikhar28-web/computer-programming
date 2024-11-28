# Write a function to find the union of two lists.

def list_union(lst1, lst2):
    return list(set(lst1) | set(lst2))

print(list_union([1, 2, 3], [2, 3, 4]))  