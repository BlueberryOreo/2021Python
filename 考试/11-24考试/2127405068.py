#  学号:2127405068
#  姓名:孙家扬
#  IP:192.168.156.99
#  上传时间:2021/11/24 19:27:32

import math


def func1(a, b):
    if a <= 0 or b <= 0:
        return False
    factor_a = []
    factor_b = []
    for i in range(1, a + 1):
        if a % i == 0:
            factor_a.append(i)
    for i in range(1, b + 1):
        if b % i == 0:
            factor_b.append(i)

    #print(factor_a)
    #print(factor_b)
    flag = True
    for i in factor_a:
        if i == 1:
            continue
        if i in factor_b:
            flag = False
            break
    return flag

def func2(num):
    temp = list(str(num))
    if len(temp) % 2 != 0:
        ret = int(temp[len(temp) // 2])
    else:
        ret = False
    return ret


def func3(n):
    cups = n // 10
    m = 0
    while cups >= 5:
        m += 3
        cups -= 5
    while cups >= 3:
        m += 1
        cups -= 3
    return m + n // 10
    

def func4(r, x, y):
    if r <= 0 or x <= 0 or y <= 0:
        return False

    d = math.sqrt(x ** 2 + y ** 2)
    if d < r:
        ret = 1
    elif d == r:
        ret = 2
    elif d > r:
        ret = 3
    return ret


def func5(n, m):
    count = 0
    for i in range(min(m, n), max(m, n) + 1):
        temp = list(str(i))
        reversed_temp = list(reversed(temp))
        if temp == reversed_temp:
            count += 1
    return count


def func6(n):
    def f(x):
        ret = 1
        for i in range(1, x + 1):
            ret *= i
        return ret

    result = list(str(f(n)))
    result.reverse()
    count = 0
    for i in range(len(result)):
        if result[i] == "0":
            count += 1
        else:
            break
    return count


def func7(lst):
    if lst == []:
        return lst
    
    nums_j = []
    nums_o = []
    for i in lst:
        if i % 2 == 0:
            nums_o.append(i)
        else:
            nums_j.append(i)

    nums_j.sort()
    nums_o.sort(reverse=True)
    return nums_j + nums_o


def func8(lst):
    dic = {}
    for i in lst:
        keys = list(dic.keys())
        if i not in keys:
            dic[i] = 1
        else:
            dic[i] += 1
            
    keys = list(dic.keys())
    m_lst = []
    m = keys[0]
    for k in keys:
        if dic[k] > dic[m]:
            m = k
    for k in keys:
        if dic[k] == dic[m]:
            m_lst.append(k)
            
    if len(m_lst) > 1:
        m_lst.sort(reverse=True)
        return m_lst
    else:
        return m


if __name__ == "__main__":
    print("func1", func1(-4, -8))
    print("func1", func1(48, 14))
    print("func1", func1(55, 23))
    print("func1", func1(1, 1))
    print("func1", func1(11, 12))
    print("func1", func1(100, 24))

    print("func2", func2(123))
    print("func2", func2(95134))
    print("func2", func2(12345))
    print("func2", func2(5555))

    print("func3", func3(10))
    print("func3", func3(30))
    print("func3", func3(50))
    print("func3", func3(80))
    print("func3", func3(100))

    print("func4", func4(-1, 2, 3))
    print("func4", func4(5, 3, 4))
    print("func4", func4(6, 6, 6))
    print("func4", func4(10, 6, 6))
    print("func4", func4(5, 5, 1))

    print("func5", func5(6718, 40))
    print("func5", func5(2852, 7066))
    print("func5", func5(100, 101))
    print("func5", func5(10, 100))

    print("func6", func6(36))
    print("func6", func6(83))
    print("func6", func6(100))
    #print("func6", func6(3600))

    print("func7", func7([3,0,7,8]))
    print("func7", func7([1,9,7,4,3]))
    print("func7", func7([]))
    print("func7", func7([1, 1, 5, 7, 10, 2, 4]))

    print("func8", func8([1, 1, 5, 7, 10, 2, 4]))
    print("func8", func8([60, 36, 1, 49, 35, 35]))
    print("func8", func8([69, 69, 70, 2, 42, 69, 88, 91, 6]))
    print("func8", func8([15, 29, 69, 93, 3]))
    print("func8", func8([95, 95, 39, 12, 12, 23, 15, 15]))
    print("func8", func8([1, 4, 4, 5, 5, 7, 7, 2, 1]))
    
