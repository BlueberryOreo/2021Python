with open("./students_data.txt", encoding="UTF-8") as f:
    lines = f.readlines()

f_out = open("./students_5.txt", "wt")
for l in lines:
    temp = l.split()
    if int(temp[-1]) > 3:
        f_out.write(temp[0] + " " + temp[1] + "\n")

f_out.close()
