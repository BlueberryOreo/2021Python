goods = {"apple": 5, "orange": 3, "phone": 5000, "PC": 8000, "pear": 4, "potato": 3}

keys = list(goods.keys())
for i in range(len(keys)):
    print(i + 1, keys[i], goods[keys[i]])

shopping_car = {}
index = int(input())
while index != 0:
    shopping_keys = list(shopping_car.keys())
    if keys[index - 1] not in shopping_keys:
        shopping_car[keys[index - 1]] = goods[keys[index - 1]]
    else:
        shopping_car[keys[index - 1]] += goods[keys[index - 1]]
    index = int(input())

print("{:>9}{:>9}{:>9}{:>9}".format("名称", "单价", "数量", "小计金额"))
shopping_keys = list(shopping_car.keys())
s = 0
for k in shopping_keys:
    print("{:>10}{:>10}{:>10}{:>12}".format(k, goods[k], shopping_car[k] // goods[k], shopping_car[k]))
    s += shopping_car[k]
print("\t\t\t\t\t\t\t共计金额：" + str(s))
