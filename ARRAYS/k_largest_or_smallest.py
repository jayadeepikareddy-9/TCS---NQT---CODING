def kLargeOrSmall(arr, k):
    arr.sort()
    print(arr[k-1])
    print(arr[-k])
kLargeOrSmall([1, 2, 3, 4, 5], 2)