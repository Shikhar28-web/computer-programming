# Write a function to find the union of two lists.

def find_union(list1, list2):
    return list(set(list1) | set(list2))

print(find_union([1, 2, 3], [2, 3, 4]))  
