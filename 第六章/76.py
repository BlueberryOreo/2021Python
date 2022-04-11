dic1 = {"key1": 1, "key2": 2, "key3": 3}
dic2 = {"key2": 2, "key3": 3, "key4": 4}

keys1 = list(dic1.keys())
keys2 = list(dic2.keys())

common = set()
for k1 in keys1:
    for k2 in keys2:
        if dic1[k1] == dic2[k2]:
            common.add(k1)
            common.add(k2)

print(common)
