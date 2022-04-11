choose = int(input("请选择你最喜欢的编程语言\n[1]Python\n[2]C++\n[3]Java\n[4]退出\n"))
if choose == 1:
    output = "Python"
elif choose == 2:
    output = "C++"
elif choose == 3:
    output = "Java"
elif choose == 4:
    print("退出成果")
    exit(0)
else:
    print("选择有误")
    exit(0)

print(output + "是一款非常优秀的编程语言")