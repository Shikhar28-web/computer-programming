# Write a function to count the occurrences of each element in a list.

def count_occurrences(lst):
    return {item: lst.count(item) for item in lst}

print(count_occurrences([1, 2, 2, 3, 4, 4, 5])) 