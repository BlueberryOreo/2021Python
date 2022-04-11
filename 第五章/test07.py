excellent = 0
passed = 0
fail = 0

score = int(input())
while score > 0:
    if score >= 90:
        excellent += 1
    elif 60 <= score < 90:
        passed += 1
    elif score < 60:
        fail += 1
    score = int(input())

print("excellent:", excellent, " passed:", passed, " fail:", fail)