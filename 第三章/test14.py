def queue(s):
    lst = s.split(" ")
    return [lst[1], lst[2]]


name = ["张飞 78 75", "李大刀 92 67", "李墨白 84 88", "王老虎 84 50", "雷小米 92 98"]
name.sort(key=queue, reverse=True)
# 等同于
# name.sort(key=lambda x: [x.split(" ")[1], x.split(" ")[2]], reverse=True)
for i in name:
    print(i)
