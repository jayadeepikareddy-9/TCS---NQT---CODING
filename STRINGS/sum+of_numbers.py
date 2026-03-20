def sumOfNumbers(s):
    total = 0
    num = 0
    for c in s:
        if c.isdigit():
            num = num*10 + int(c)
        else:
            total += num
            num = 0
    total += 0
    total += num
    return total
s = "abc123def45gh6"
print(sumOfNumbers(s))
