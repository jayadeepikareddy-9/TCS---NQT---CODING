def symmetricArray(arr):
    print("Symmetric Array:")
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[j][0] == arr[i][1] and arr[j][1] == arr[i][0]:
                print(arr[i][1], arr[i][0])
print(symmetricArray([[1, 2], [2, 3], [3, 4], [4, 1], [2, 1], [4, 3]]))

