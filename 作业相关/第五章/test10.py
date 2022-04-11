data = {"LiKe": 19, "TangYi": 18, "MeiYuyao": 18,
        "SunZonglei": 19, "ZhangRuyue": 18, "XuYifan": 18,
        "LuZhangjun": 18, "JiangXinyuan": 17, "WuYicun": 18, "ShenLeyao": 17}

maxes = []
max_age = list(data.keys())[0]
for k in data.keys():
    if data[k] > data[max_age]:
        max_age = k
        maxes.clear()
        maxes.append(k)
    elif data[k] == data[max_age]:
        maxes.append(k)

for m in maxes:
    print(m, data[m])
