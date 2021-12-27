s = input()
minus = s.split('-')
ans = []
for m in minus:
    t = m.split('+')
    tmp = 0
    for i in t:
        tmp += int(i)
    ans.append(tmp)
rst = ans[0]
for i in ans[1:]:
    rst -= i
print(rst)