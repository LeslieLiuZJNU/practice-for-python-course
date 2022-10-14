# match = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
# x = int(input("请输入一个三位数："))
# a = x // 100
# b = x % 100 // 10
# c = x % 10
# print("所需火柴棍的数量：", match[a] + match[b] + match[c])
#
# match = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
# x = input("请输入一个三位数：")
# a = int(x[0])
# b = int(x[1])
# c = int(x[2])
# print("所需火柴棍的数量：", match[a] + match[b] + match[c])
#
# match = {0: 6, 1: 2, 2: 5, 3: 5, 4: 4, 5: 5, 6: 6, 7: 3, 8: 7, 9: 6}
# x = int(input("请输入一个三位数："))
# a = x // 100
# b = x % 100 // 10
# c = x % 10
# print("所需火柴棍的数量：", match[a] + match[b] + match[c])

match = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
x = int(input("请输入要求的火柴棍数："))
for i in range(100, 1000):
    a = i // 100
    b = i % 100 // 10
    c = i % 10
    if match[a] + match[b] + match[c] == x:
        print("符合要求的第一个三位数为：", i)
        break
