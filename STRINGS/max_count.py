s = input()
max_char = ''
max_count = 0

for c in s:
    count = s.count(c)
    if count > max_count:
        max_count = count
        max_char = c

print(max_char)