def f(l_s: str, n: int):
    if n >= len(l_s):
        return None
    lst = list(l_s)
    lst.remove(lst[n - 1])
    return "".join(lst)

if __name__ == "__main__":
    s = input()
    n = int(input("删去第几个字符？"))
    print(f(s, n))
