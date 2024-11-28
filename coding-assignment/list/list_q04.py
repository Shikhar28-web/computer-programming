# Write a function to check if a list is a sublist of another list.
def is_sublist(lst, sublist):
    sub_len = len(sublist)
    return any(sublist == lst[i:i + sub_len] for i in range(len(lst) - sub_len + 1))

print(is_sublist([1, 2, 3, 4], [2, 3]))  
