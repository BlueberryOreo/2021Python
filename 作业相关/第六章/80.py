name = ("DaiYuan", "LiChenggeng", "WangXun", "ZhangMingming", "XuSiyi", "XueGuangquan", "TangSujuan", "WuJiajun")
age = (18, 18, 18, 17, 17, 18, 18, 21)

dic = {name[i]: age[i] for i in range(len(name))}
print(dic)
