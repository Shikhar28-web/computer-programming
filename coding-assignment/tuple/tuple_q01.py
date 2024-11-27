# Create a Python program that merges two tuples without using built-in functions and returns the result.

def merge_tuples(t1, t2):
    result = ()
    for item in t1:
        result += (item,)
    for item in t2:
        result += (item,)
    return result

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
print(merge_tuples(tuple1, tuple2))  
