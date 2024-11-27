#Write a function to find the longest palindromic substring in a given string.

def longest_palindromic_substring(s):
    n = len(s)
    table = [[False] * n for _ in range(n)]

    maxLength = 1
    start = 0

    for i in range(n):
        table[i][i] = True

    for i in range(n - 1):
        if s[i] == s[i + 1]:
            table[i][i + 1] = True
            start = i
            maxLength = 2

    for k in range(3, n + 1):
        for i in range(n - k + 1):
            j = i + k - 1
            if table[i][j - 1] and s[i] == s[j]:
                table[i][j] = True
                if k > maxLength:
                    start = i
                    maxLength = k

    return s[start:start + maxLength]


print(longest_palindromic_substring("babad"))  
