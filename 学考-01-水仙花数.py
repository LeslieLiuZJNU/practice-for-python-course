x = int(input("请输入一个三位数："))
a = x // 100
b = x % 100 // 10
c = x % 10
if a ** 3 + b ** 3 + c ** 3 == x:
    print("是")
else:
    print("否")
