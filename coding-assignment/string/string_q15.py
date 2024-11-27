# Write a function to find the length of the longest substring without repeating characters.
def longest_unique_substring(s):
    n = len(s)
    max_len = 0
    start = 0
    char_index = {}
    
    for end in range(n):
        if s[end] in char_index:
            start = max(start, char_index[s[end]] + 1)
        char_index[s[end]] = end
        max_len = max(max_len, end - start + 1)
    
    return max_len


print(longest_unique_substring("abcabcbb")) 