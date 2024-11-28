# Write a function to flatten a nested list.

def flatten_list(nested_list):
    flat_list = []
    for sublist in nested_list:
        for item in sublist:
            flat_list.append(item)
    return flat_list

print(flatten_list([[1, 2], [3, 4], [5]]))  
