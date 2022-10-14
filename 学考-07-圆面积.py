from math import pi
from math import pow


def area(R):
    S = pi * pow(R, 2)
    return S


L = int(input("请输入圆的直径："))
print(area(L / 2))
