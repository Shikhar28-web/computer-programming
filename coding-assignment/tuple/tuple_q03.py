# Develop a Python script to find the second largest number in a tuple of integers.


def second_largest(t):
    unique_sorted = sorted(set(t), reverse=True)
    return unique_sorted[1] if len(unique_sorted) > 1 else None

my_tuple = (3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5)
print(second_largest(my_tuple)) 
