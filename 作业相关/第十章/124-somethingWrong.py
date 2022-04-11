flag = True
source = input("请输入源文件路径：")
while flag:
    try:
        f_in = open(source, encoding="UTF-8")
        lines = f_in.readlines()
    except FileNotFoundError:
        source = input("源文件不存在，请重新输入：")
    except UnicodeDecodeError:
        try:
            f_in = open(source, encoding="ASCII")
        except UnicodeDecodeError:
            print("文件无法用UTF-8编码或ASCII编码打开！")
            flag = False
    else:
        flag = False

flag = True
target = input("请输入目的文件路径：")
while flag:
    try:
        f_out = open(target, "a+")
        f_out.write("\n")
        for l in lines:
            f_out.write(l)
    except Exception:
        target = input("目的文件不可写，请重新输入文件路径：")
    else:
        flag = False

