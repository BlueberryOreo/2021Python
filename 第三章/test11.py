str1 = input("str1 = ")
str2 = input("str2 = ")

flag = True
if len(str1) != len(str2):
    flag = False
else:
    lst1 = list(str1)
    lst2 = list(str2)
    lst1.sort()
    lst2.sort()
    if lst1 != lst2:
        flag = False

print("输入的两个字符串同构" if flag else "输入的两个字符串不同构")
