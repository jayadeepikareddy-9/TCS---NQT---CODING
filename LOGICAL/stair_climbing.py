#staircase when you can take 1 or 2 steps
n = int(input())
a, b = 1, 1
for i in range(n):
    a,b = b, a+b
print(a)

n = int(input())

a, b = 1, 2

for i in range(3, n+1):
    c = a + b
    a = b
    b = c

print(b if n > 1 else 1)


#staircase when you can take 1, 2, or 3 steps
n = int(input())

if n == 1:
    print(1)
elif n == 2:
    print(2)
elif n == 3:
    print(4)
else:
    a, b, c = 1, 2, 4
    for i in range(4, n+1):
        d = a + b + c
        a = b
        b = c
        c = d
    print(c)