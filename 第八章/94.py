def f(l_s: str):
    if len(l_s) < 2:
        return ""
    else:
        return l_s[:2] + l_s[-2:]

if __name__ == "__main__":
    s = input()
    print(f(s))
