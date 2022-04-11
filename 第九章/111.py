import re


num = re.compile(r"-?\d+")

with open("./StrInts.txt") as f:
    lines = f.readlines()

nums = []
for l in lines:
    nums += list(map(int, num.findall(l)))

print(nums)
f_out = open("./ResultInts.txt", "wt")
count = 0
for n in nums:
    flag = True if abs(n) > 10 else False
    start = 1 if n > 0 else 2
    for i in range(start, len(str(n)), 2):
        if int(str(n)[i]) % 2 == 0:
            flag = False
            break
    if flag:
        f_out.write("{:>8}".format(n))
        count += 1
    if count == 3:
        f_out.write("\n")
        count = 0
f_out.close()
