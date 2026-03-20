def missing(arr):
    n = len(arr) + 1
    expected = n * (n + 1) // 2
    actual = sum(arr)
    return expected - actual
arr = [1, 2, 4, 5]
print(missing(arr))

#Method 2: XOR Trick
arr = list(map(int, input().split()))
n = len(arr) + 1

xor_all = 0
xor_arr = 0

for i in range(1, n+1):
    xor_all ^= i

for x in arr:
    xor_arr ^= x

print(xor_all ^ xor_arr)

#using set
arr = list(map(int, input().split()))
n = len(arr) + 1

s = set(arr)

for i in range(1, n+1):
    if i not in s:
        print(i)
        break