from collections import defaultdict

def count_frequency(arr):
    n = len(arr)
    freq = defaultdict(int)
    for i in range(n):
        freq[arr[i]] +=1

    for key, value in freq.items():
        print(key,value)

print(count_frequency([1,2,3,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5]))



