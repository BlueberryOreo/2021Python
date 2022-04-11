import datetime

d1 = datetime.datetime.now()
d2 = datetime.datetime(1970, 1, 1)
print((d1 - d2).days, "days", d1.strftime("%H"), "hours")
