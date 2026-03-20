def ascii(s):
    result = ord(s)
    print(result)

ascii('a')
ascii('b')
ascii('c')
ascii('d')
ascii('A')
ascii('B')
ascii('C')
ascii('Z')

def character(n):
    result = chr(n)
    print(result)

character(97)
character(98)
character(99)
character(100)

s = input("Enter string: ")

vowels = "aeiouAEIOU"

for ch in s:
    if ch not in vowels:
        print(ch, end="")