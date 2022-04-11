characters = input("请输入一些大写字母：")

dic = {}
for c in characters:
    keys = list(dic.keys())
    if c not in keys:
        dic[c] = 1
    else:
        dic[c] += 1

keys = list(dic.keys())
for i in keys:
    print(i, ":", dic[i], end=", ")
