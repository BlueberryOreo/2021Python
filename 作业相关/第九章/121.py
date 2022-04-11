with open("./Names.txt") as f:
    names = f.read().split("\n")

insert = input("请输入要插入的名字：")
names.append(insert)
# print(names)
names.sort(key=lambda n: ord(n[0]))
f = open("./Names.txt", "w+")
for n in names:
    f.write(n)
    f.write("\n" if names.index(n) < len(names) - 1 else "")
f.close()
