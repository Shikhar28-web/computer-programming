# Write a function to rotate a list to the right by k elements.

def rotate_list(lst, k):
    k = k % len(lst)  
    return lst[-k:] + lst[:-k]

print(rotate_list([1, 2, 3, 4, 5], 2))  
