import os

files = os.listdir("./Folder")
print(files)
f_out = open("./Folder/merge.txt", "wt")
for f in files:
    temp = open("./Folder/" + f)
    for l in temp.readlines():
        f_out.write(l if l.endswith("\n") else l + "\n")
f_out.close()
