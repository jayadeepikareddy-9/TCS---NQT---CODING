def removeSpaces(s):
    result = []
    for c in s:
        if c != ' ' and c != '\t' and c != '\n':
            result.append(c)
    return "".join(result)
        
s = "Hello World"
print(removeSpaces(s))


def removeSpaces(s):
    return s.replace(" ", "")
s = "JAYA DEEPIKA REDDY CHALLA"
print(removeSpaces(s))