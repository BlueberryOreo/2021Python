import math

x1 = float(input("x1 = "))
y1 = float(input("y1 = "))
r = float(input("r = "))

x2 = float(input("x2 = "))
y2 = float(input("y2 = "))

d = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

if d <= r:
    print("坐标点({},{})在圆内".format(x2, y2))
else:
    print("坐标点({},{})不在圆内".format(x2, y2))