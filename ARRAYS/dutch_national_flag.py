def dutch(arr):
    n = len(arr)
    low = 0
    high = n-1
    mid = 0
    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1 
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1

if __name__ == "__main__":
    arr = [1,2,0,1,0,2,1]
    dutch(arr)
    for i in range(len(arr)):
        print(arr[i], end=" ")