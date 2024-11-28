# Discuss the defaultdict from the collections module and provide examples

from collections import defaultdict

my_defaultdict = defaultdict(list)
my_defaultdict['a'].append(1)
my_defaultdict['b'].append(2)
print(my_defaultdict)  

count_dict = defaultdict(int)
count_dict['a'] += 1
count_dict['b'] += 2
print(count_dict)  
