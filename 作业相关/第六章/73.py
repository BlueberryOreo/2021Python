import random

score = [random.randint(0, 10) for i in range(7)]
# print(score)

score.remove(max(score))
score.remove(min(score))

average = sum(score) / len(score)
# print(score)
print(average)
