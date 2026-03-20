def removeNonAlphas(s):
    for ch in s:
        if ('a' <= ch <= 'z') or ('A' <= ch <= 'Z'):
            print(ch, end="")
s = input("Enter string: ")
removeNonAlphas(s)