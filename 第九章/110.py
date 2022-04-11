f1 = open("./cat2.txt")
f2 = open("./cat1.txt", "a+")

lines = f1.readlines()
for l in lines:
    f2.write(l)

f1.close()
f2.close()
