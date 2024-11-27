# Write a function to restore possible valid IP addresses from a string.

def restore_ip_addresses(s):
    def backtrack(start, path):
        if len(path) == 4:
            if start == len(s):
                result.append('.'.join(path))
            return
        
        for length in range(1, 4):
            if start + length <= len(s):
                part = s[start:start + length]
                if (part[0] == '0' and len(part) == 1) or (part[0] != '0' and 0 <= int(part) <= 255):
                    backtrack(start + length, path + [part])
    
    result = []
    backtrack(0, [])
    return result

print(restore_ip_addresses("25525511135"))  
