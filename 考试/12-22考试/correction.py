def func3_c(num):
    def is_prime(n):
        if n == 1 or n == 0 or int(n) != n:
            return False
        flag = True
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                flag = False
                break
        return flag

    for i in range(2, num // 2 + 1):
        if is_prime(i) and is_prime(num / i):
            return True
    return False


def func1_c(s1, s2):
    import re
    m = re.compile(r"[^a-zA-Z]")
    if m.findall(s1) or not s1.endswith(s2):
        return False
    else:
        return True


if __name__ == "__main__":
    print("f1", func1_c("abdeded", "ded"))
    print("f1", func1_c("12334sdsds", "ded"))
    print("f1", func1_c("asdefd", "asasdefd"))
    print("f1", func1_c("d.2ds3ded", "ded"))
    # for i in range(1, 5000):
    #     print("f3", i, func3_c(i))
