time1 = input().split(":")
time2 = input().split(":")

timeList1 = list(map(int, time1))
timeList2 = list(map(int, time2))

# print(timeList1, timeList2)
interval = (timeList2[0] - timeList1[0]) * 3600 + (timeList2[1] - timeList1[1]) * 60 + (timeList2[2] - timeList1[2])
print(interval)
