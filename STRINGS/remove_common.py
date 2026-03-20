def removeChar(str1, str2):
    removed = str(str2)
    result = ""
    for ch in str1:
        if ch not in str2:
            result += ch
    return result
str1 = "hello world"
str2 = "lo"
print(removeChar(str1, str2))