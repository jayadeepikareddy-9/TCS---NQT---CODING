s = list(input())
for i in range(len(s)):
    if s[i] == 'z':
        s[i] == 'a'
    else:
        s[i] = chr(ord(s[i]) + 1)
print(''.join(s))