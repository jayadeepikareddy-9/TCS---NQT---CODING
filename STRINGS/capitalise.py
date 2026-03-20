def capitalize(s):
    words = s.split()   
    result =[]
    for word in words:
        if len(word) <= 1:
            result.append(word.upper())
        else:
            new_word = word[0].upper() + word[1:-1] + word[-1].upper()
            result.append(new_word) 
    return ' '.join(result)
s = "hello world"
print(capitalize(s))