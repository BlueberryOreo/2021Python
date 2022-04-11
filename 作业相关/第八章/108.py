import re

user_name_j = re.compile(r"^[^a-zA-Z-]|[^a-zA-Z\d-]")
password_j1 = re.compile(r"[a-z]")
password_j2 = re.compile(r"[A-Z]")
password_j3 = re.compile(r"\d")

user_name = input("请输入用户名(长度大于等于6，不能以数字开头，不能包含!？@等符号，-除外)：")
while len(user_name) < 6 or user_name_j.findall(user_name):
    user_name = input("不满足条件，请重新输入：")

password = input("请输入密码(长度大于等于6，只能使用数字、大写英文字母和小写英文字母，且必须同时使用这3种字符)：")
while not (password_j1.findall(password) and password_j2.findall(password) and password_j3.findall(password) and len(password) >= 6):
    # print(bool(password_j1.findall(password)), bool(password_j2.findall(password)), bool(password_j3.findall( \
    # password)))
    password = input("不满足条件，请重新输入")

password_confirmed = input("请确认密码：")
while password_confirmed != password:
    password_confirmed = input("密码错误，请重新输入：")

print(user_name, password)
