# with open("./config.txt", "wt") as f:
#     for i in range(65, 91):
#         f.write(chr(i) + ":" + chr(i + 32))
#         f.write("\n" if i < 90 else "")

with open("./config.txt") as f:
    lines = f.read().split("\n")

new_config = open("./new_config.txt", "wt")
for l in lines:
    temp = l.split(":")
    new_config.write("<{}>".format(temp[0]) + temp[1] + "</{}>".format(temp[0]))
    new_config.write("\n")

new_config.close()
