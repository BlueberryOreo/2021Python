import re

with open("./article.txt") as f:
    context = f.read()

context = list(context)
temp = ""
new_lst = []
for c in context[:]:
    if c in [".", "!", "?"]:
        temp += c
        new_lst.append(temp)
        temp = ""
        continue
    if c == "\n":
        context.remove(c)
        temp += " "
    else:
        temp += c

for n in new_lst:
    print(n)

with open("./new_article.txt", "w+") as f:
    for s in new_lst:
        if s.startswith(" "):
            temp = list(s[1:])
        else:
            temp = list(s)
        temp[0] = temp[0].upper()
        f.write("".join(temp))
        f.write("\n")
