def change(c: str, form):
    if form == 1:
        c = c.lower()
    elif form == 2:
        c = c.upper()
    return c


if __name__ == "__main__":
    # print(change("a", 2))
    string = list(input())
    choose = int(input("1->转换小写\t2->转换大写\n"))
    for s in string:
        print(change(s, choose), end="")
