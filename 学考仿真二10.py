s = "China"
t = [1, 3, 2]
res = ""
for i in range(len(s)):
    m = t[i % len(t)]
    n = ord(s[i]) + m
    res = res + chr(n)
print(res)
