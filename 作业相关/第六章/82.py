
dic = {}

while True:
    data = input("请输入姓名和编号，用空格隔开，输入stop结束输入：")
    if data == "stop":
        break
    data = data.split()
    dic[data[0]] = data[1]

form = int(input("请选择以怎样的形式输出，1.按姓名顺序；2.按编号顺序："))
if form == 1:
    keys = list(dic.keys())
    for k in keys:
        print("{:<20}{:<20}".format(k, dic[k]))
elif form == 2:
    reversed_dic = {dic[k]: k for k in list(dic.keys())}
    keys = list(reversed_dic.keys())
    for k in keys:
        print("{:<15}{:<15}".format(k, reversed_dic[k]))
