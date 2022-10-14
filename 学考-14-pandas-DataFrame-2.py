import pandas as pd

df = pd.read_excel("scores.xls")
df_add = df.append(
    {"姓名": "刘思远", "班级": "03", "总分": 100, "信息技术客观分": 24, "信息技术主观分": 26, "通用技术客观分": 26,
     "通用技术主观分": 24}, ignore_index=True)
df_delc = df.drop("信息技术客观分", axis=1).drop("信息技术主观分", axis=1).drop("通用技术客观分", axis=1).drop(
    "通用技术主观分", axis=1)
df_delr = df.drop(0)

g = df.groupby("班级", as_index=False)
print(g.mean())

df_sort = df.sort_values("总分", ascending=False)
print(df_sort)
