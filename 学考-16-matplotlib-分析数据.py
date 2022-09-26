import pandas as pd
import matplotlib.pyplot as plt
import codecs
from matplotlib.font_manager import FontProperties

file = codecs.open("xm.csv", "r", "utf-8")
# 定义复姓 list
fx = ["欧阳", "太史", "端木", "上官", "司马", "东方", "独孤", "南宫", "万俟", "闻人", "夏侯", "诸葛", "尉迟", "公羊",
      "赫连", "皇甫", "濮阳", "公冶", "申屠", "公孙", "慕容", "钟离", "长孙", "宇文", "司徒", "鲜于", "司空", "闾丘",
      "子车", "亓宫", "宰父", "谷梁", "拓跋", "轩辕", "令狐", "百里", "呼延", "东郭", "南门", "羊舌", "公仪", "西门",
      "第五"]
xing = []
for line in file:
    if line[0:2] in fx:
        xing.append(line[0:2])
    else:
        xing.append(line[0:1])
data = {"xing": xing, "renshu": 0}
df = pd.DataFrame(data)
s = df.groupby("xing").count()
s = s.sort_values("renshu", ascending=False)
ax = s[0:20].plot(kind="bar", rot=0)
font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=12)
for label in ax.get_xticklabels():
    label.set_fontproperties(font)
plt.show()
print(s)
