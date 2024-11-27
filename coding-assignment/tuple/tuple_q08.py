# Write a Python script to combine a tuple of strings into a single string with a given delimiter.


def join_tuple_strings(t, delimiter):
    return delimiter.join(t)

my_tuple = ('a', 'b', 'c')
print(join_tuple_strings(my_tuple, '-'))  # Output: a-b-c
