total = 0
everyMonth = 100
base = 0
n = 5
for i in range(n):
    base += everyMonth
    total = (everyMonth + total) * (1 + 0.005)

print("{:>4.5f} {:>4.2f}%".format(total, (total - base) / base * 100))
