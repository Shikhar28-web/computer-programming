# Write a function to compress a string using the counts of repeated characters.


def compress_string(s):
    if not s:
        return ""
    
    result = []
    count = 1
    
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            result.append(s[i - 1] + str(count))
            count = 1
    
    result.append(s[-1] + str(count))
    compressed = ''.join(result)
    
    return compressed if len(compressed) < len(s) else s


print(compress_string("aabcccccaaa")) 