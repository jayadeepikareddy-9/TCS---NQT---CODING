def removeBrackets(s):
    stack = [1]
    sign = 1
    result = ""

    for i in range(len(s)):
        if s[i] == '+':
            sign = stack[-1]
            result += '+' if sign == 1 else '-'

        elif s[i] == '-':
            sign = -stack[-1]
            result += '-' if sign == 1 else '+'

        elif s[i] == '(':
            stack.append(sign)

        elif s[i] == ')':
            stack.pop()

        else:
            result += s[i]

    return result


s = "a-(b+c)"
print(removeBrackets(s))