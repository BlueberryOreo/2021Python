n = int(input("请输入一个0-100的整数："))
if n < 0 or n > 100:
    print("你输入的数不在0-100范围内！")
    exit(0)

if n % 3 == 0:
    print("可以被3整除")
else:
    print("不能被3整除")
