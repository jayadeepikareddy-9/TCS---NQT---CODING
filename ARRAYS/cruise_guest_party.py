def entryExit(entry, exit):
    entry.sort()
    exit.sort()
    i = j = 0
    count = 0
    max_guests = 0
    while i < len(entry) and j < len(exit):
        if entry[i] <= exit[j]:
            count += 1
            max_guests = max(max_guests, count)
            i += 1
        else:
            count -= 1
            j += 1  
    return max_guests
entry = [1, 1, 1]
exit = [2, 3, 4]
print(entryExit(entry, exit))


