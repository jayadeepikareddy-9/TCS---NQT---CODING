def average(arr):
    n = len(arr)
    total = n
    for i in range(n):
        total = total + arr[i]
    return total/n
print(average([1,2,3,4,5,6,7,8,9,10]))

def median(arr,n):
    arr.sort()
    if n%2 == 0:
        ind1 = (n//2)-1
        ind2 = (n//2)
        print((arr[ind1]+arr[ind2])/2)
    else:
        print(arr[n//2])

arr = [1,2,3,4,5,6,7,8,9,10]
n = len(arr)
median(arr,n)


      
