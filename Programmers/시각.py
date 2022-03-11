n = int(input())
ans = 0
for i in range(n+1):
    for j in range(60):
        for k in range(60):
           if str(n) in str(i)+str(j)+str(k):
               ans += 1
print(ans) 