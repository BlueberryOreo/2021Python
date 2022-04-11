# import random
#
# with open("./largefile.txt", "w+", encoding="ASCII") as f:
#     count = 0
#     r = random.randint(40, 70)
#     for i in range(100000):
#         f.write(chr(random.randint(48, 126)))
#         count += 1
#         if count == r:
#             f.write("\n")
#             count = 0
#             r = random.randint(40, 70)


file = open("./largefile.txt", "rb")
file.seek(0, 2)
length = file.tell()
file.seek(0, 0)
col = []
start = 0
line_length = 0
p = 0
for p in range(length):
    current = file.read(1)
    if current == b"\r":
        continue
    elif current == b"\n":
        col.append((start, line_length))
        start = p + 1
        line_length = 0
        continue
    line_length += 1
col.append((start, length - start))
# print(col[-1])
# print(p, length)
# print(col)
# print(len((col)))
# file.seek(260, 0)
# print(file.read(50))
print("largefile.txt一共有{}行".format(len(col)))
while True:
    l = int(input("请输入一个行号："))
    if l > len(col):
        print("超出范围！")
        continue
    file.seek(col[l - 1][0], 0)
    print(str(file.read(col[l - 1][1]))[2:-1])
file.close()
