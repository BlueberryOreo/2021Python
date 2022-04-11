import random

set1 = {random.randint(0, 500) for i in range(random.randint(200, 1000))}
set2 = {random.randint(0, 500) for i in range(random.randint(200, 1000))}

difference = []
same = []

for i in set1:
    if i not in set2:
        difference.append(i)
    else:
        same.append(i)
for i in set2:
    if i not in set1:
        difference.append(i)

count = 0
for i in difference:
    print("{:>5}".format(i), end="")
    count += 1
    if count == 10:
        print()
        count = 0

print()
count = 0
for i in same:
    print("{:>5}".format(i), end="")
    count += 1
    if count == 10:
        print()
        count = 0