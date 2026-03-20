def nonrepeating(string):
    freq = [0]*256
    for ch in string:
        freq[ord(ch)] += 1
    for ch in string:
        if freq[ord(ch)] == 1:
            print(ch, end='')
print(nonrepeating("helloworld"))


