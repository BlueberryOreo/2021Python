#  学号:2127405068
#  姓名:孙家扬
#  IP:192.168.157.51
#  上传时间:2021/11/22 15:06:24

import math

def func1(x):
    if x >= 0:
        y = 5 * x
    else:
        y = 3 * abs(x) + 1
    return y

def func2(x):
    if x >= 10:
        y = 10
    elif 8 <= x < 10:
        y = 8 * x ** 3
    elif 3 <= x < 8:
        y = 3 * x ** 2
    elif 0 <= x < 3:
        y = x + 1
    else:
        y = abs(x)
    return y
    
def func3(m,n):
    if m < 0 or n < 0 or m > n or not isinstance(m, int) or not isinstance(n, int):
        return None
    
    s = 0
    for i in range(m, n + 1):
        if i % 2 != 0:
            s += i
    return s
    
def func4(m,n):
    count = 0
    for i in range(m, n + 1):
        temp_lst = list(str(i))
        count += temp_lst.count("2")
    return count

def func5(num):
    if not isinstance(num, int) or num < 0:
        return None
    ret = []
    temp_lst = list(map(int, list(str(num))))
    ret.append(len(temp_lst))
    ret.append(sum(temp_lst))
    ret.append(max(temp_lst))
    return ret

def func6(m,n):
    if not isinstance(m, int) or not isinstance(n, int) or m < 0 or n < 0:
        return None
    m_lst = list(map(int, list(str(m))))
    m_lst[0] += n
    if m_lst[0] >= 10:
        m_lst[0] %= 10
    
    ret = 0
    for i in range(len(m_lst)):
        ret += m_lst[i] * 10 ** (len(m_lst) - i - 1)
    return ret
        
def func7(k, lst):
    if k >= len(lst):
        lst.reverse()
        return lst
    reversed_lst = lst[:k]
    del lst[:k]
    reversed_lst.reverse()
    return reversed_lst + lst

def func8(v, lst):
    for i in lst[:]:
        temp_lst = list(map(int, list(str(i))))
        rou = sum(temp_lst) / len(temp_lst)
        if rou < v:
            lst.remove(i)
    lst.sort(reverse=True)
    return lst

if __name__=="__main__":
    # print(func1(0))
    # print(func1(2))
    # print(func1(-1))
    # print("=" * 20)
    #
    # print(func2(15))
    # print(func2(8))
    # print(func2(3))
    # print(func2(0))
    # print(func2(-99))
    # print("=" * 20)
    #
    # print(func3(3, 12))
    # print(func3(1, 20))
    # print(func3(2.4, 4))
    # print(func3(2, 2.4))
    # print(func3(-1, 2))
    # print(func3(2, -5))
    # print(func3(5, 3))
    # print("=" * 20)
    #
    # print(func4(2, 22))
    # print(func4(2, 25))
    # print("=" * 20)
    #
    # print(func5(123))
    # print(func5(290))
    # print(func5(2.3))
    # print(func5(-2))
    # print("=" * 20)
    #
    # print(func6(345, 6))
    # print(func6(856, 70))
    # print(func6(345, 8))
    # print(func6(2.3, 5))
    # print(func6(2, 3.5))
    # print(func6(-2, 3))
    # print(func6(2, -3))
    # print("=" * 20)
    #
    # print(func7(4, [3, 4, 1, 5, 2]))
    # print(func7(5, [3, 4, 1, 5, 2]))
    # print(func7(20, [2, 3, 4, 5, 6, 7, 87]))
    # print("=" * 20)
    #
    # print(func8(4, [123, 1234, 345, 456, 567]))
    print("func4", func4(-2, 5))
