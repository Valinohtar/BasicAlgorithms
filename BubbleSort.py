lst = [9, 5, 1, 4, 6, 7, 13, 14, 2, 11, 6, 6, 6]
lst.insert(0, 0)
for i in range(1, len(lst)):
    j = i - 1
    x = lst[i]
    lst[0] = x
    while x < lst[j]: 
        lst[j+1] = lst[j]
        j -= 1
    lst[j+1] = x
lst.pop(0)
print(lst)


