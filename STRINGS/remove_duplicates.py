def removeDuplicates(s):
    result = ""
    for ch in s:
        if ch not in result:
            result += ch
    return result
s = "hello world"
print(removeDuplicates(s.replace(" ", "")))

s = input()
n = len(s)
print(2**n)