x = int(input("x = "))
y = int(input("y = "))
z = int(input("z = "))

lst = [x, y, z]
lst.sort()
for i in lst:
    print(i)

if x > y:
    if x > z:
        max = x
        if z > y:
            mid = z
            min = y
        else:
            mid = y
            min = z
    else:
        max = z
        mid = x
        min = y
else:
    if y > z:
        max = y
        if x > z:
            mid = x
            min = z
        else:
            mid = z
            min = x
    else:
        max = z
        mid = y
        min = x
print(min, mid, max)
