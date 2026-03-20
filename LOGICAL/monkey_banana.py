bananas = int(input())
k =int(input())
peels = bananas
total = bananas
while peels >= k:
    new_banana = peels // k
    total += new_banana
    peels = peels % k + new_banana
print(total)
