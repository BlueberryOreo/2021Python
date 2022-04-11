import re


def judge(l_s):
    characters = re.compile(r"\w+")
    # characters = re.compile(r"[^.,!]+")
    s_after = "".join(characters.findall(l_s)).lower()
    print(s_after)
    return s_after == s_after[::-1]


print(judge("W@#&^%ha&^&$t T^%^aH!!?,w..."))
