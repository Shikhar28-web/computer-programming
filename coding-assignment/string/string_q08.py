# Write a function to check if a string is a valid IP address.

def is_valid_ip(s):
    parts = s.split(".")
    if len(parts) != 4:
        return False

    for part in parts:
        if not part.isdigit() or not 0 <= int(part) <= 255:
            return False

    return True


print(is_valid_ip("192.168.0.1"))  