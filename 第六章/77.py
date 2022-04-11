import random

first_name = ["Xun", "Yuan", "Guanquan", "Chenggeng", "Jiayang"]
last_name = ["Wang", "Dai", "Xue", "Li", "Sun"]

dic = {}
for i in range(len(last_name)):
    dic[last_name[i] + random.choice(first_name)] = random.randint(1, 100)

print(dic)
keys = list(dic.keys())
for k in keys:
    if 0 < dic[k] < 18:
        dic.pop(k)

print(dic)
