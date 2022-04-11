import random

n = int(input())
nums = []
for i in range(n):
    nums.append(random.randint(1, 1000))

for i in nums:
    while nums.count(i) > 1:
        nums.remove(i)

nums.sort()
print(nums)
