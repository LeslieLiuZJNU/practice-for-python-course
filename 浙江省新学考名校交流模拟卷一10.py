s = input("请输入字符串:")
i = 0
j = len(s) - 1
flag = True
while i <= len(s)//2 and flag:
    if s[i] == s[j]:
        i += 1
        j -= 1
    else:
        flag = False
if flag:
    print("Yes")
else:
    print("No")
