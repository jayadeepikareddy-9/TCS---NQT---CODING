#frequency is calculated using ASCII values 
# Time complexity: O(n) where n is the length of the string
# Space complexity: O(1) since the frequency array has a fixed size of 256

def frequency(string):
    freq = [0] * 256
    for ch in string:
        freq[ord(ch)] += 1
    for i in range(256):
        if freq[i] > 0:
            print(chr(i), ":", freq[i])

frequency("hello world")

#without get method
def frequency(string):
    freq = {}
    for ch in string:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1
    print(freq)
frequency("hello world")

#using get method
def frequency(string):
    freq = {}
    for ch in string:
        freq[ch] = freq.get(ch, 0) + 1
    print(freq)
frequency("hello world")
