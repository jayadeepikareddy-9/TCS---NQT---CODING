def duplicateElement(arr):
    freq = {}
    res = []
    for i in arr:
        freq[i] = freq.get(i, 0) + 1
    for x in freq:
        if freq[x] > 1:
            res.append(x)
    return res
arr = [1, 2, 3, 4, 6, 1, 4, 2]
print(duplicateElement(arr))