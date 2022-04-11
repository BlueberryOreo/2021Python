lst = [1, 3, 4, 6, 6, 7, 8, 8, 10, 21, 22, 22]

left = 0
right = 1
while lst[right] < 10:
    if lst[left] != lst[right]:
        left += 1
        lst[left] = lst[right]
        right += 1
    else:
        right += 1
print(lst[0:left + 1])
