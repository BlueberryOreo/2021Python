
import re


def judge(l_code: str):
    num = re.compile(r"[0-9]+")
    lower = re.compile(r"[a-z]+")
    upper = re.compile(r"[A-Z]+")
    return len(l_code) > 8 and bool(num.findall(l_code)) and bool(lower.findall(l_code)) and bool(upper.findall(l_code))


if __name__ == "__main__":
    code = input()
    print(judge(code))
