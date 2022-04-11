import os
import datetime


def iter_dir(root_dir):
    files = []
    subs = os.listdir(root_dir)
    for f in subs:
        sub_path = os.path.join(root_dir, f)
        if os.path.isdir(sub_path):
            files += iter_dir(sub_path)
        if os.path.isfile(sub_path):
            files.append(sub_path)
    return files


def delete(file_paths: list):
    log = open("./log.txt", "a+")
    print(file_paths)
    for f in file_paths:
        if f.endswith(".tmp"):
            t = datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S")
            try:
                os.remove(f)
                log.write("{} DELETE SUCCESS {}".format(t, f) + "\n")
            except OSError:
                log.write("{} DELETE FAIL {}".format(t, f) + "\n")
    log.close()


# f_out = open("./test.txt", "wt")
g_root_dir = input("请输入要删除.tmp文件的文件夹路径：")
g_files = iter_dir(g_root_dir)
# for i in g_files:
#     print(i, file=f_out)
# f_out.close()
delete(iter_dir(g_root_dir))
