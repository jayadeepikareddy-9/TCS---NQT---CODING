def swapcase(s):
    result = ""
    for ch in s:
        if ch.islower():
            result += ch.upper()
        else:
            result += ch.lower()
    return result
s = "HeLLO wORLd"
print(swapcase(s))