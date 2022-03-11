n = int(input())
scores = []
for _ in range(n):
    name, k, e, m = map(str, input().split())
    scores.append([name,int(k),int(e),int(m)])
scores.sort(key=lambda x:(-x[1],x[2],-x[3],x[0]))
# 이렇게 해도 돼
# scores.append([name, k, e, m])
# scores.sort(key=lambda x:(-int(x[1]),int(x[2]),-int(x[3]),x[0]))
for s in scores:
    print(s[0])