lst = [35, 46, 57, 13, 24, 35, 99, 68, 13, 79, 88, 46]

# 法一：
new_lst = []
for i in lst:
    if i not in new_lst:
        new_lst.append(i)
new_lst.sort()
print(new_lst)

# 法二：
i = 0
j = 1
lst.sort()
while j != len(lst):
    if lst[i] != lst[j]:
        i += 1
        lst[i] = lst[j]
        j += 1
    else:
        j += 1
print(lst[:i + 1])

# 法三：
for i in lst:
    while lst.count(i) != 1:
        lst.remove(i)
print(lst)
