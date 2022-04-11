answer = input("Confirm? (Y[es] or N[o])")
if answer in ["Y", "Yes", "YES", "yes"]:
    print("Confirmed")
elif answer in ["N", "No", "NO", "no"]:
    print("Not Confirmed")
else:
    print("输入错误")