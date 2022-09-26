m = int(input("请输入m："))
n = int(input("请输入n："))
for i in range(m, n + 1):
    print(str(i) + "的因数为：", end="")
    for j in range(1, i + 1):
        if i % j == 0:
            print(str(j), end=" ")
    print()
