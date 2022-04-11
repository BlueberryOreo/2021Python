import math


def is_rt(sides: list):
    c = max(sides)
    sides.remove(c)
    if abs((sides[0] ** 2 + sides[1] ** 2) - c ** 2) < 1e-9:
        return True
    else:
        return False


if __name__ == "__main__":
    x1 = float(input("x1 = "))
    y1 = float(input("y1 = "))
    x2 = float(input("x2 = "))
    y2 = float(input("y2 = "))
    x3 = float(input("x3 = "))
    y3 = float(input("y3 = "))

    side1 = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    side2 = math.sqrt((x1 - x3) ** 2 + (y1 - y3) ** 2)
    side3 = math.sqrt((x2 - x3) ** 2 + (y2 - y3) ** 2)

    sides = [side1, side2, side3]

    s = (side1 + side2 + side3) / 2
    area = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))
    if area != 0:
        if side1 == side2 == side3:
            print("是等边三角形")
        elif is_rt(sides):
            print("是直角三角形")
        else:
            print("是其他三角形")
    else:
        print("不能构成三角形")
