def priorElement(arr):
    res = []
    for i in range(len(arr)):
        count = 0
        for j in range(i):
            if arr[j] < arr[i]:
                count += 1
        res.append(count)
    return res
arr = []
print(priorElement(arr))