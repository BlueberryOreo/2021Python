data = (65.5, 70.2, 100.5, 45.5, 88.8, 55.5, 73.5, 67.8)

average = sum(data) / len(data)

s = 0
for d in data:
    s += (average - d) ** 2

variance = s / len(data)
print(variance)
