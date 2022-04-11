dic1 = {"key1": 1, "key2": 2, "key3": 3}
dic2 = {"key2": 2, "key3": 3, "key4": 4}

keys1 = list(dic1.keys())
keys2 = list(dic2.keys())

common = []
for k in keys1:
    if k in keys2:
        common.append(k)

print(common)
