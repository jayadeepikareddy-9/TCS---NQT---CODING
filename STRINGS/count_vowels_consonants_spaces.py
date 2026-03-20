def count(s):
    s = s.lower()
    vowels = 0
    consonants = 0
    spaces = 0

    for ch in s:
        if ch in 'aeiou':
            vowels += 1
        elif 'a' <= ch <= 'z':
            consonants += 1
        elif ch == ' ':
            spaces += 1
    print("Vowels:", vowels)
    print("Consonants:", consonants)
    print("Spaces:", spaces)
# Example usage
count(" Hello  Hindustan")