with open("./word.txt") as f:
    lines = f.readlines()

f_out = open("./new_word.txt", "wt")
for l in lines[:]:
    if not l[0] in ["a", "e", "i", "o", "u"]:
        continue
    f_out.write(l)
