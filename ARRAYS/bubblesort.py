def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1, -1, -1):
        for j in range(i):
            if arr[j]> arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

arr = [5, 3, 8, 4, 2]

print(bubble_sort(arr))

def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr  
arr = [5, 3, 8, 4, 2]

print(selection_sort(arr))

def insertionSort(arr):
    n = len(arr)
    for i in range(1,n):
        key = arr[i]
        j = i - 1
        while j >=0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr
arr = [5, 3, 8, 4, 2]

print(insertionSort(arr))