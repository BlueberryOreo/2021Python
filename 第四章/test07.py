import random

num = random.randint(0, 100)
print(num)
input_num = int(input("请猜一个1-100以内的数字："))
if input_num < 0 or input_num > 100:
    print("输入错误！")
else:
    if input_num == num:
        print("恭喜，猜正确了")
    elif input_num > num:
        print("大了")
    else:
        print("小了")
