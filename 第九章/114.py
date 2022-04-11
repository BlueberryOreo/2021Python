with open("./students_data.txt", encoding="UTF-8") as f:
    students = list(map(lambda x: x.split(), f.read().split("\n")))

students.sort(key=lambda l: int(l[0]))
for s in students:
    print("{:<10}{:<15}{:>5}".format(s[0], s[1], s[2]))

s1 = int(input("请输入指定学号："))
for s in students[:]:
    if int(s[0]) < s1:
        students.remove(s)

for s in students:
    print("{:<10}{:<15}{:>5}".format(s[0], s[1], s[2]))
