lst = ["张三", "李四", "王五"]
last_name = ["" for i in range(len(lst))]
for i in lst:
    last_name[lst.index(i)] = i[0]
print(last_name)
