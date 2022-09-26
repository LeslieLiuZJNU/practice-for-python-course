import pandas as pd

data = {"姓名": ["陈佳宜", "陈军建", "陈霖恺"], "班级": ["17", "14", "14"], "总分": [89, 83, 86]}
df1 = pd.DataFrame(data, columns=["姓名", "班级", "总分"])
print(df1)

df = pd.read_excel("scores.xls")
print(df)

for i in df1.index:
    print(i)

for i in df1.columns:
    print(i)

for i in df1.values:
    print(i)

print(df1.T)

print(df1.姓名)
print(df1["总分"])
df1.总分 = [30, 52, 68]
print(df1)
