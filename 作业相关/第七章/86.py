import itertools

nums = [i for i in range(8)]
out = list(itertools.permutations(nums, 8))
count = 0
for t in out[:]:
    if t[0] == 0:
        out.remove(t)
    elif t[-1] in [1, 3, 5, 7]:
        count += 1
print(count)
