def smallest(arr):
    n = len(arr)
    min = arr[0]
    for i in range(n):
        if arr[i]< min:
            min = arr[i]
    return min
print(smallest([1,4,2,3,6,0]))

def smallest(arr):
    n = len(arr)
    max = arr[0]
    for i in range(n):
        if arr[i]> max:
            max = arr[i]
    return max
print(smallest([1,4,2,3,6,0]))

def second_smallest(arr):
    n = len(arr)
    small = float('inf')
    second_small = float('inf')
    for i in range(n):
        if arr[i] < small:
            second_small = small
            small = arr[i]
        elif arr[i] < second_small and arr[i] != small:
            second_small = arr[i]
    return second_small
print(second_smallest([1,3,2,6,8,4,5,7]))

def second_largest(arr):
    n = len(arr)
    large = float('-inf')
    second_large = float('-inf')
    for i in range(n):
        if arr[i] > large:
            second_large = large
            large = arr[i]
        elif arr[i] > second_large and arr[i] != large:
            second_large = arr[i]
    return second_large
print(second_largest([1,3,2,9,8,5,7]))