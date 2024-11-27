# Write a function to find the longest common prefix string amongst an array of strings.

def longest_common_prefix(strs):
    if not strs:
        return ""

    prefix = strs[0]
    for s in strs[1:]:
        while s.find(prefix) != 0:
            prefix = prefix[:-1]
            if not prefix:
                return ""

    return prefix

print(longest_common_prefix(["flower", "flow", "flight"])) 
