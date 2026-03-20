def uniqueElement(arr):
    freq = {}
    for i in arr:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    for key, value in freq.items():
        if value == 1:
            return key
    return -1
arr = [1, 2, 3, 2, 1]
print(uniqueElement(arr))   