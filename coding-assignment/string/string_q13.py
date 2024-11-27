# Write a function to remove duplicate characters from a string.


def remove_duplicates(s):
    result = []
    seen = set()
    
    for char in s:
        if char not in seen:
            result.append(char)
            seen.add(char)
    
    return ''.join(result)


print(remove_duplicates("aabb[_{{{CITATION{{{_1{](https://github.com/hauphanlvc/CS112.L22/tree/f3856f9f4cb7f627176774b83da9426aec959e22/ChuoiConDoiXungDaiNhat.py")