with open("./article.txt") as f:
    lines = f.read().split("\n")

dic = dict()

for l in lines:
    temp = l.split()
    for t in temp:
        if {".", ",", "?", "!"} & set(t):
            t = t[:-1]
        keys = list(dic.keys())
        if len(t) in keys:
            dic[len(t)].append(t)
        else:
            dic[len(t)] = [t]

sorted_keys = sorted(dic)
f_out = open("./new_article_classify.txt", "wt")
for k in sorted_keys:
    words = ",".join(dic[k])
    f_out.write(str(k) + ":" + str(len(dic[k])) + " " + words)
    f_out.write("\n")

f_out.close()
