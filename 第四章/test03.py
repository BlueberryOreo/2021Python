num = input("请输入一个不多于５位的正整数：")
if int(num) < 0:
    print("不是正整数！")
    exit(0)
elif len(num) > 5:
    print("输入的数超过了５位！")
    exit(0)

print("{}是{}位数".format(int(num), len(num)))
for i in num:
    print(i)

str = list(num)
str.reverse()
for i in str:
    print(i, end="")