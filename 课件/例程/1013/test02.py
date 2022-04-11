# 计算过两点A(x1,y1)，B(x2,y2)的圆的最小面积，其中x1 != x2 或 y1 != y2
import math

x1 = float(input("x1 = "))
y1 = float(input("y1 = "))
x2 = float(input("x2 = "))
y2 = float(input("y2 = "))

while x1 == x2 and y1 == y2:
    print("输入的点为同一个点，请重新输入！")
    x1 = float(input("x1 = "))
    y1 = float(input("y1 = "))
    x2 = float(input("x2 = "))
    y2 = float(input("y2 = "))

r = 0.5 * (math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)))
s = math.pi * r * r
print("最小的圆的面积为：",s)