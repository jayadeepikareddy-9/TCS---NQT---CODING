def equilibriumIndex(arr):
    totalSum = sum(arr)
    leftSum = 0
    rightSum = totalSum
    n = len(arr)
    for i in range(n):
        rightSum -= arr[i]
        if leftSum == rightSum:
            return i
        leftSum += arr[i]
    return -1
arr = [-7, 1, 5, 2, -4, 3, 0]
print(equilibriumIndex(arr))