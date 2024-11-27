# Write a function that sorts a list of tuples based on the second element of each tuple.

def sort_by_second(tuples_list):
    return sorted(tuples_list, key=lambda x: x[1])

my_tuples = [(1, 3), (3, 2), (2, 1)]
print(sort_by_second(my_tuples))  