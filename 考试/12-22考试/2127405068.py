#  学号:2127405068
#  姓名:孙家扬
#  IP:192.168.157.19
#  上传时间:2021/12/22 19:42:31

import math


def func1(s1, s2):
    import re
    m = re.compile(r"\d")
    if m.findall(s1):
        return False
    if s1.endswith(s2):
        return True
    else:
        return False


def func2(n, m):
    count = 0
    for i in range(n, m + 1):
        if len(str(i)) == 3 and i % 2 != 0:
            count += 1
    return count


def func3(num):
    def is_prime(n):
        flag = True
        for i in range(2, int(n ** 0.5)):
            if n % i == 0:
                flag = False
                break
        return flag

    count = 0
    for i in range(2, num):
        if num % i == 0 and is_prime(i):
            count += 1
    return count == 2


def func4(lst):
    for i in lst[:]:
        if len(str(i[0])) != 3 or not 0 <= i[1] <= 100 or not 0 <= i[2] <= 100:
            lst.remove(i)
    lst.sort(key=lambda x: (x[1] + x[2], x[1], -x[0]), reverse=True)
    return lst if lst else [[]]


def func5(s):
    dic = {}
    for i in s:
        keys = dic.keys()
        if i not in keys:
            dic[i] = 1
        else:
            dic[i] += 1
    ret = tuple(sorted(filter(lambda k: dic[k] % 2 == 0, dic.keys())))
    return ret if ret else -1


def func6(strn):
    import re
    m = re.compile(r"\d+")
    ret = "".join(m.findall(strn))
    return int(ret) if ret else None


def func7(s1, s2, s3):
    c1 = s1 & s3
    c2 = s2 & s3
    if len(c1) < len(c2):
        ret = (1, len(s1 | s3) + len(s2))
    elif len(c2) < len(c1):
        ret = (2, len(s2 | s3) + len(s1))
    else:
        ret = (0, len(s1 | s3) + len(s2))
    return ret


def func8(strn, t):
    start = 0
    end = 1
    dic = {}
    while end < len(t):
        if t[start] < len(strn) and t[end] < len(strn):
            temp = strn[min(t[start], t[end]):max(t[start], t[end]) + 1]
            for c in temp:
                keys = dic.keys()
                if c not in keys:
                    dic[c] = 1
                else:
                    dic[c] += 1
        start += 1
        end += 1
    ret = sorted(dic.items(), key=lambda x: (x[1], -ord(x[0])))
    return ret


if __name__ == '__main__':
    print("f1", func1("abdeded", "ded"))
    print("f1", func1("abded", "def"))
    print("f1", func1("abded", "ded1"))
    print("=" * 20)
    print("f2", func2(20, 103))
    print("f2", func2(100, 105))
    print("f2", func2(200, 300))
    print("=" * 20)
    print("f3", func3(15))
    print("f3", func3(5))
    print("f3", func3(27))
    print("=" * 20)
    print("f4", func4([[105, 4, 3], [104, 4, 3], [102, 4, 3]]))
    print("f4", func4([[2, 3, 5], [100, 3, 4], [101, 4, 3]]))
    print("f4", func4([[2, 3, 5], [100, 173, 4], [101, -1, 3]]))
    print("=" * 20)
    print("f5", func5([3, 61, 4]))
    print("f5", func5([56, 56, 2, 1, 2, 3, 2, 3, 4]))
    print("f5", func5([-1, -1, 2, 2, -3, -3]))
    print("f5", func5([]))
    print("=" * 20)
    print("f6", func6("xyzxc"))
    print("f6", func6("0x0y0z0"))
    print("f6", func6("-123"))
    print("f6", func6("$a+0b/1c-2d+-"))
    print("=" * 20)
    print("f7", func7({1, 2}, {3, 4}, set()))
    print("f7", func7({1, 2}, {3, 4}, {1, 2}))
    print("f7", func7(set(), set(), set()))
    print("=" * 20)
    print("f8", func8("abcbbcxy666678$", (3, 1, 10)))
    print("f8", func8("abcSxy678$", (3, 10, 5)))
    pass
