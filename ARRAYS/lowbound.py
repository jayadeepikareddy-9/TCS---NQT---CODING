def lower_bound(arr, target):
    for i in range(len(arr)):
        if arr[i] >= target:
            return i
    return len(arr)

arr = [1, 2, 5, 8, 15]
target = 9
index = lower_bound(arr, target)
print(index)  # Output: 3, since arr[3] = 7 is the first element greater than or equal to 6


class LowerBoundFinder:
    # Method to find lower bound index
    def lower_bound(self, arr, x):
        for i in range(len(arr)):
            if arr[i] >= x:
                return i  # First index where element >= x
        return len(arr)  # If x is greater than all elements

# Driver code
arr = [3, 5, 8, 15, 19]
x = 9

finder = LowerBoundFinder()
ind = finder.lower_bound(arr, x)

print("The lower bound is the index:", ind)

class UpperBoundFinder:
    # Linear search to find upper bound
    def upper_bound(self, arr, x):
        for i in range(len(arr)):
            if arr[i] > x:
                return i  # First element greater than x
        return len(arr)   # Return size if no such element found

# Driver code
arr = [3, 5, 8, 9, 15, 19]  # Sorted array
x = 9

finder = UpperBoundFinder()
ind = finder.upper_bound(arr, x)

print("The upper bound is the index:", ind)
