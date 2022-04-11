def output(title, item):
    print("{:<6}".format(title), end="")
    if isinstance(item, list):
        for i in item:
            print("{:<6}".format(i), end="")
    else:
        print(" ", end="")
        for i in range(item):
            print("{:<7}".format(i + 1), end="")
    print()
    return

name = ["张三", "李四", "王五", "赵六", "孙七", "周八", "吴九"]
odd = []
even = []

for i in range(len(name)):
    if (i + 1) % 2 == 0:
        even.append(name[i])
    else:
        odd.append(name[i])

output("分组", max(len(odd), len(even)))
output("奇数组", odd)
output("偶数组", even)
