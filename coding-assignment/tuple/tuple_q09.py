# Write a function that takes a tuple and an integer n, and returns a new tuple with the first n elements removed.

def remove_first_n(t, n):
    return t[n:]

my_tuple = (1, 2, 3, 4, 5)
print(remove_first_n(my_tuple, 2))  
