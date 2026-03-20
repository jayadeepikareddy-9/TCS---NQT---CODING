money = int(input())
cost = int(input())
wrap = int(input())

chocolates = money // cost
wrappers = chocolates
total = chocolates

while wrappers >= wrap:
    new_choco = wrappers // wrap
    total += new_choco
    wrappers = wrappers % wrap + new_choco

print(total)
