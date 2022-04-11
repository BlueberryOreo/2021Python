import datetime

# 总耗时，换算成秒
totalTime = 100 / 80 * 3600

# 建立一个列表用于储存总耗时（时，分，秒）
times = [0 for i in range(3)]
n = 2
while totalTime > 0:
    # 通过数学的方法从秒推断出小时和分钟，并依次存到列表中
    times[n] = totalTime % 60
    totalTime //= 60
    n -= 1

# print(times)
# 获取当前时间，并格式化时间（时 分 秒），然后分开当前时间的字符串获得当前时间的
# 时、分、秒的一个列表
nowTime = list(map(int, datetime.datetime.now().strftime("%H %M %S").split(" ")))
# 计算到达时间，通过列表各个元素对应加起来
arrivalTime = [nowTime[0] + times[0], nowTime[1] + times[1], nowTime[2] + times[2]]
# 分钟大于60，小时+1，分钟60
if arrivalTime[1] >= 60:
    arrivalTime[0] += 1
    arrivalTime[1] -= 60
# 打印，格式化输出
print("{:02.0f}:{:02.0f}:{:02.0f}".format(arrivalTime[0], arrivalTime[1], arrivalTime[2]))
