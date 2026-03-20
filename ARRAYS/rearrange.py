def rearrangeArray(arr):
    arr.sort()
    n = len(arr)
    arr[n//2:] = reversed(arr[n//2:])
    return arr
print(rearrangeArray([1, 2, 3, 4, 5, 6, 7]))


def sumOfArray(arr):
    return sum(arr)
print(sumOfArray([1, 2, 3, 4, 5, 6, 7]))

def sumOfArray(arr):
    sum = 0
    for i in arr:
        sum += i
    return sum
print(sumOfArray([1, 2, 3, 4, 5, 6, 7]))