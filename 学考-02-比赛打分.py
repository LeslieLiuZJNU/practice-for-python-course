score = [72, 84, 68, 77, 56, 82, 85, 79, 76, 81]
sum = 0
for i in range(0, 10):
    sum = sum + score[i]
print("总和为：", sum)

score = [72, 84, 68, 77, 56, 82, 85, 79, 76, 81]
max = -1
for i in range(0, 10):
    if score[i] > max:
        max = score[i]
print("最大分为：", max)

score = [72, 84, 68, 77, 56, 82, 85, 79, 76, 81]
min = 101
for i in range(0, 10):
    if score[i] < min:
        min = score[i]
print("最小分为：", min)

score = [72, 84, 68, 77, 56, 82, 85, 79, 76, 81]
sum = 0
max = -1
min = 101
for i in range(0, 10):
    sum = sum + score[i]
    if score[i] > max:
        max = score[i]
    if score[i] < min:
        min = score[i]
print("最终得分为：", (sum - max - min) / 8)
