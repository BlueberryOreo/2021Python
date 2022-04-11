import re


def reformat(s):
    compare_space = re.compile(r"\b\s{2,}")
    compare_punctuation = re.compile(r"[^\w\s']\w")
    changed = compare_space.sub(" ", s)
    # print(compare_punctuation.search(changed))
    while compare_punctuation.search(changed):
        start = compare_punctuation.search(changed).start()
        # end = compare_punctuation.search(changed).end()
        temp = list(changed)
        temp.insert(start + 1, " ")
        changed = "".join(temp)
        print(changed)
    return changed


if __name__ == "__main__":
    g_s = input()
    print(reformat(g_s))

# This  is  very,funny,and,cool.Indeed!
