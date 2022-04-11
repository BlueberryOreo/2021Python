store = int(input("请输入存款金额（单位：万元）："))
accrual = 0.0
if store < 10:
    accrual = 0.015
elif 10 <= store < 50:
    accrual = 0.02
elif 50 <= store < 100:
    accrual = 0.03
elif store >= 100:
    accrual = 0.035

print(store * (1 + accrual))
