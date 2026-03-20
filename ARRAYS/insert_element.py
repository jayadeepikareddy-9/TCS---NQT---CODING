def insertElement(arr, element):
    arr.insert(0, element)
    arr.insert(3, element)
    return arr

print(insertElement([1,2,3,4,5,6,7], 10))