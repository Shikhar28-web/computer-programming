# Write a program to count the frequency of each element in a list using a dictionary.


my_list = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
freq_dict = {}
for item in my_list:
    if item in freq_dict:
        freq_dict[item] += 1
    else:
        freq_dict[item] = 1
print(freq_dict)  