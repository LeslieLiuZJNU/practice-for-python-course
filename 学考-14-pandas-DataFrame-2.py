import pandas as pd

df = pd.read_excel("scores.xls")  # 读excel表，文件名为“scores.xls”

# df = df.append(
#     {"姓名": "刘思远", "班级": "03", "总分": 10, "信息技术客观分": 1, "信息技术主观分": 2, "通用技术客观分": 6,
#      "通用技术主观分": 1}, ignore_index=True)
# df_delc = df.drop("信息技术客观分", axis=1).drop("信息技术主观分", axis=1).drop("通用技术客观分", axis=1).drop(
#     "通用技术主观分", axis=1)

# df_delr = df.drop(0)
#
# g = df.groupby("班级", as_index=False)
# print(g.mean()) # mean() 平均数
#
df_sort = df.sort_values("总分", ascending=False) # 降序排序
print(df_sort)
