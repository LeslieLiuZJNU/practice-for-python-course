import pandas as pd

s1 = pd.Series([89, 87, 86])
print(s1)

s2 = pd.Series([89, 87, 86], index=["陈佳宜", "张启航", "陈霖恺"])
print(s2)

for i in s1.index:
    print(i)

for i in s1.values:
    print(i)

for i in s1:
    print(i)
