IPv4 = input().split(".")
flag = True
type = None
for i in range(len(IPv4)):
    if not IPv4[i].isdigit():
        flag = False
        break
    if int(IPv4[i]) >= 255 or int(IPv4[i]) <= 0 or len(IPv4) != 4:
        flag = False
        break
    if i == 0:
        temp = int(IPv4[0])
        if 0 < temp <= 127:
            type = "A"
        elif 128 <= temp <= 191:
            type = "B"
        elif 192 <= temp <= 223:
            type = "C"
        elif 224 <= temp <= 239:
            type = "D"
        elif 240 <= temp <= 254:
            type = "F"

if flag:
    print(type)
else:
    print("该地址不合法！")