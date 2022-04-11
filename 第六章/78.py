
# def encode(x):
#     return x ** 3 - 25


code = {}
# 创建密码字典
# 字符
# for i in range(65, 91):
#     code[format(i, 'c')] = i
# for i in range(97, 123):
#     code[format(i, 'c')] = i
for i in range(32, 48):
    code[format(i, 'c')] = i
for i in range(58, 127):
    code[format(i, 'c')] = i
# 数字
for i in range(48, 58):
    code[format(i, 'c')] = format(i - 10, 'c')

d_code = {v: k for k, v in code.items()}
# print(d_code)


def encode(s: str):
    ret = ""
    for i in s:
        ret += str(code[i])
    return ret


def decode(s: str):
    ret = ""
    start = 0
    end = 0
    while end < len(s):
        end += 1
        temp = s[start:end]
        try:
            if 32 <= int(temp) <= 48 or 58 <= int(temp) <= 127:
                ret += d_code[int(temp)]
                start = end
        except ValueError:
            ret += d_code[temp]
            start = end
    return ret


'''
count = 0
for k in list(code.keys()):
    print(k, code[k], end="\t")
    count += 1
    if count == 5:
        print()
        count = 0
'''
choice = int(input("请输入你需要的功能（1.加密；2.解密）"))
if choice == 1:
    s = input("请输入要加密的字符串：")
# for i in s:
#     print(code[i], end="")
    print(encode(s))
elif choice == 2:
    s = input("请输入要解密密码：")
    print(decode(s))
else:
    print("输入有误！")
