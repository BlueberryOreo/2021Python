# import os
#
# files = os.listdir("./")
# with open("./filenames.txt", "wt") as f:
#     for file in files:
#         if len(file) > 8:
#             continue
#         f.write(file + "\n")
import re


with open("./filenames.txt") as f:
    lines = f.read().split("\n")

for i in range(len(lines)):
    print("./" + lines[i])
    f = open("./" + lines[i] + ".txt", "wt")
    f.write(lines[i - 1])
    f.close()
