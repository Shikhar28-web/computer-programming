# Write a function to simplify a Unix-style path.


def simplify_path(path):
    parts = path.split('/')
    stack = []
    
    for part in parts:
        if part == '..':
            if stack:
                stack.pop()
        elif part and part != '.':
            stack.append(part)
    
    return '/' + '/'.join(stack)


print(simplify_path("/a/./b/../../c/")) 
