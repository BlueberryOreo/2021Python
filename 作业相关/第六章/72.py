lst = ["alpha", "all", "dig", "date", "egg"]
dic = {}

for i in lst:
    keys = list(dic.keys())
    if i[0] not in keys:
        dic[i[0]] = [i]
    else:
        dic[i[0]].append(i)

print(dic)
