# from random import randint
# from random import shuffle
#
# classes = ["高二（1）班", "高二（2）班", "高二（3）班", "高二（4）班", "高二（5）班"]
# print("随机抽取一个班级：", classes[randint(0, 4)])
# shuffle(classes)
# print("随机安排出场顺序：", classes)

from random import choice
from random import shuffle

classes = ["高二（1）班", "高二（2）班", "高二（3）班", "高二（4）班", "高二（5）班"]
print("随机抽取一个班级：", choice(classes))
shuffle(classes)
print("随机安排出场顺序：", classes)
