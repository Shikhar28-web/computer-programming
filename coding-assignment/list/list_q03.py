# Write a function to find the frequency of elements in a list.

def frequency_of_elements(lst):
    return {item: lst.count(item) for item in set(lst)}

print(frequency_of_elements([1, 2, 2, 3, 4, 4, 5])) 
