# Write a function to find the second largest number in a list.


def second_largest(numbers):
    unique_numbers = list(set(numbers))
    unique_numbers.sort()
    return unique_numbers[-2]

print(second_largest([1, 2, 3, 4, 5]))  
