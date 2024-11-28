# Describe how to iterate over keys, values, and key-value pairs in a dictionary.



my_dict = {'a': 1, 'b': 2, 'c': 3}

for key in my_dict:
    print(key)

for value in my_dict.values():
    print(value)

for key, value in my_dict.items():
    print(f'Key: {key}, Value: {value}')
