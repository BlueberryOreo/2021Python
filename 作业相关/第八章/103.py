def interchange(a, b, s: str):
    if a < 2 or a > 16 or b < 2 or b > 16:
        return None
    dec = int(s, a)
    ret = []
    while dec > 0:
        if b <= 2:
            ret.append(dec % b)
        else:
            temp = dec % b
            if temp >= 10:
                ret.append(chr(temp + 55))
            else:
                ret.append(temp)
        dec //= b
    return "".join(list(map(str, ret[::-1])))


if __name__ == "__main__":
    print(interchange(4, 8, "11111"))
    print(interchange(10, 3, "10"))
