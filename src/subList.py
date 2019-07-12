def isSubList(a, b):
    if len(a) > len(b):
        return False
    for i in range(0, len(b) - len(a) + 1):
        if b[i:i+len(a)] == a:
            return True
    return False