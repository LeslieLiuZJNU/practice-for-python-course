def convert(s):
    m = int(s[0:2]) * 3600 + int(s[3:5]) * 60 + int(s[6:8])
    return m


def select(stu):
    x = list(stu.items())
    x.sort(key=lambda x: x[1], reverse=True)
    print("上周班级阅读之星：")
    for i in range(len(x)):
        if i >= 5 and x[i][1] != x[i - 1][1]:
            break
        print("姓名：" + x[i][0], "阅读总时长：" + str(x[i][1]))


file = open("data.csv")
line = file.readline()
stu = {}
while line:
    info = line.split(",")
    t = convert(info[3]) - convert(info[2])
    if info[0] in stu:
        stu[info[0]] += t
    else:
        stu[info[0]] = t
    line = file.readline()
file.close()
select(stu)
