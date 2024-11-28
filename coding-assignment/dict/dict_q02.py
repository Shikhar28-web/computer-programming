# Explain how to handle KeyError exceptions when accessing dictionary elements.


my_dict = {'a': 1, 'b': 2, 'c': 3}
try:
    value = my_dict['d']
except KeyError:
    value = None
print(value)  
