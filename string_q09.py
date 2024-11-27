# Write a function to generate all substrings of a string.

def all_substrings(s):
    return [s[i:j] for i in range(len(s)) for j in range(i + 1, len(s) + 1)]


print(all_substrings("abc")) 