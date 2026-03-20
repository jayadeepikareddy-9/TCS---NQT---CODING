def rotateArray(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

def left_rotate(arr,d):
    n = len(arr)
    d = d % n
    if d == 0:
        return
    rotateArray(arr, 0, d-1)
    rotateArray(arr, d, n-1)
    rotateArray(arr, 0, n-1)

arr = [1, 2, 3, 4, 5, 6, 7]
d = 2
left_rotate(arr, d)
print(arr)


def right_rotate(arr, d):
    n = len(arr)
    d = d % n
    if d == 0:
        return
    rotateArray(arr, 0, n-1)
    rotateArray(arr, 0, d-1)
    rotateArray(arr, d, n-1)

arr = [1, 2, 3, 4, 5, 6, 7]
d = 2
right_rotate(arr, d)
print(arr)
