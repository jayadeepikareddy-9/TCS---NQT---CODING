def reverse_array(arr):
    n = len(arr)
    left = 0
    right = n-1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left +=1
        right -=1
    return arr
print(reverse_array([4,5,6,7,8]))