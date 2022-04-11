import random

users = ["JiangZijian 12345", "DaiYuan 23456", "ZhangMingming 43254", "SunJiayang 021010"]
identifying_code = random.randint(1000, 9999)
information = input("请输入用户名　密码：")
id_code = int(input("请输入验证码[{}]".format(identifying_code)))
if information in users and id_code == identifying_code:
    print("登陆成功！")
else:
    if information not in users:
        print("用户名或密码不正确！")
    else:
        print("验证码有误！")
