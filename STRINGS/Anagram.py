def anagram(s1, s2):
    return sorted(s1) == sorted(s2)
print(anagram("listen", "silent"))  # True
print(anagram("hello", "world"))    # False


s1 = input()
s2 = input()
freq = {}
for ch in s1:
    freq[ch] = freq.get(ch, 0) + 1
for ch in s2:
    freq[ch] = freq.get(ch,0) - 1
for key in freq:
    if freq[key] != 0:
        print("Not Anagram")
        break
else:   
    print("Anagram")

