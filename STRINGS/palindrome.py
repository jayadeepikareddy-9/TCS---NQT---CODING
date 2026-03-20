def palindrome(s):
    left = 0
    right = len(s)-1
    Flag = True

    while left < right:
        if s[left] != s[right]:
            Flag = False 
            break
        left += 1
        right -= 1

    if Flag:
        print("Palindrome")
    else:
        print("Not a palindrome")

# Example usage
palindrome("maadaam")