# Function to find repeating elements in the array
def findRepeatingElements(arr):
    arr.sort()  # Sort the array to easily find duplicates
    
    print("The repeating elements are:", end=" ")
    for i in range(len(arr) - 1):
        # If current element is equal to next element, it's a repeating element
        if arr[i] == arr[i + 1]:
            print(arr[i], end=" ")

# Driver code
arr = [1, 1, 2, 3, 4, 4, 5, 2]  # Example input
findRepeatingElements(arr)  # Call the function to find repeating elements

#OPTIMAL SOLUTION
from collections import Counter

def findRepeatingElements(arr):
    elementCount = Counter(arr)
    print("The repeating elements are:", end=" ")
    for key, value in elementCount.items():
        if value > 1:
            print(key, end=" ")

arr = [1, 1, 2, 3, 4, 4, 5, 2]  # Example input
findRepeatingElements(arr)  # Call the function to find repeating elements
