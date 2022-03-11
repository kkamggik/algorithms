s1,s2 = map(str, input().split())
ans = 0
if len(s1)==len(s2):
    for i in range(len(s1)):
        if s1[i] != s2[i]: ans += 1
else:
    ans = 1e9
    if len(s2) < len(s1):
        s1,s2 = s2,s1
    for i in range(len(s2)-len(s1)+1):
        cnt = 0
        for j in range(len(s1)):
            if s1[j] != s2[j+i]: cnt += 1
        ans = min(ans, cnt)
print(ans)