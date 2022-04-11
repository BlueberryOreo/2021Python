import re


def func(s1: str, s2: str):
    return "".join(re.split(r"[{}]".format(s1), s2))


s_lst = input()
filter_str = input()
# for c in s_lst[:]:
#     if c in filter_str:
#         s_lst.remove(c)
#
# print("".join(s_lst))
print(func(filter_str, s_lst))
