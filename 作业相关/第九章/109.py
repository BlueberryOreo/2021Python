
# f_in = open("copy.txt")
# f_out = open("new.txt", "wt")
# lines = f_in.readlines()
# f_in.close()
#
# print(type(lines), lines)
# for l in lines:
#     f_out.write(l)
# f_out.close()

global f_in
global f_out

try:
    f_in = open("copy.txt")
    f_out = open("new.txt", "wt")
    lines = f_in.readlines()

    for l in lines:
        f_out.write(l)
except FileNotFoundError as e:
    print(e)
finally:
    f_in.close()
    f_out.close()
