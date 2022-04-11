s = input()
dic = {}
for c in s:
    keys = list(dic.keys())
    if c not in keys:
        dic[c] = 1
    else:
        dic[c] += 1
print(str(dic)[1:-1])
