# Write a function to sort a list in descending order.

def sort_list_descending(lst):
    return sorted(lst, reverse=True)

print(sort_list_descending([3, 1, 4, 1, 5, 9]))  