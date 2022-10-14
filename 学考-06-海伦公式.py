# a = int(input("请输入第1个三角形的第1个边长："))
# b = int(input("请输入第1个三角形的第2个边长："))
# c = int(input("请输入第1个三角形的第3个边长："))
# d = int(input("请输入第2个三角形的第1个边长："))
# e = int(input("请输入第2个三角形的第2个边长："))
# f = int(input("请输入第2个三角形的第3个边长："))
# g = int(input("请输入第3个三角形的第1个边长："))
# h = int(input("请输入第3个三角形的第2个边长："))
# i = int(input("请输入第3个三角形的第3个边长："))
# p1 = (a + b + c) / 2
# s1 = (p1 * (p1 - a) * (p1 - b) * (p1 - c)) ** 0.5
# print("第1个三角形的面积为：", s1)
# p2 = (d + e + f) / 2
# s2 = (p2 * (p2 - a) * (p2 - b) * (p2 - c)) ** 0.5
# print("第2个三角形的面积为：", s2)
# p3 = (g + h + i) / 2
# s3 = (p3 * (p3 - a) * (p3 - b) * (p3 - c)) ** 0.5
# print("第3个三角形的面积为：", s3)
#

def area(a, b, c):
    p = (a + b + c) / 2
    s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    return s


for i in range(1, 4):
    a = int(input("请输入第" + str(i) + "个三角形的第1个边长："))
    b = int(input("请输入第" + str(i) + "个三角形的第2个边长："))
    c = int(input("请输入第" + str(i) + "个三角形的第3个边长："))
    print("第" + str(i) + "个三角形的面积为：", area(a, b, c))
