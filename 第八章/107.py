import re


def number(l_num: str):
    phone_number = re.compile(r"^1\d{10}")
    telephone_number = re.compile(r"^0\d{2,3}?-?[^0]\d{6,7}")
    special_number = re.compile(r"1\d{2}")

    if phone_number.match(l_num):
        return "手机号码"
    elif telephone_number.match(l_num):
        return "国内固定电话"
    elif special_number.match(l_num) and len(num) == 3:
        return "特殊号码"
    else:
        return None


if __name__ == "__main__":
    num = input()
    print(number(num))
