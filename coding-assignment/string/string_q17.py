# Write a function to count the number of non-empty substrings that have the same number of 0s and 1s.


def count_binary_substrings(s):
    groups = []
    count = 1
    
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            groups.append(count)
            count = 1
    groups.append(count)
    
    result = 0
    for i in range(1, len(groups)):
        result += min(groups[i - 1], groups[i])
    
    return result


print(count_binary_substrings("00110011"))  
