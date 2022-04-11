# import random
#
# with open("./Numbers.txt", "wt") as f:
#     for i in range(100):
#         f.write(str(random.uniform(1, 100)))
#         f.write("\n")


with open("./Numbers.txt") as f:
    nums = list(map(float, f.readlines()))

nums.sort()
f_out = open("./Sort.txt", "wt")
s = 0
for n in nums:
    f_out.write(str(n) + "\n")
    s += n

average = s / len(nums)
temp = 0
for n in nums:
    temp += (n - average) ** 2
variance = temp / len(nums)

f_out.write("Average=" + str(average) + "\n" + "Variance=" + str(variance))
f_out.close()