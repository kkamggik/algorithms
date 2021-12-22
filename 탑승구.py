def find(x):
    if parent[x]!=x:
        parent[x] = find(parent[x])
    return parent[x]
def union(a,b):
    x = find(a)
    y = find(b)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y
n = int(input())
p = int(input())
parent = [i for i in range(n+1)]
ans = 0
arr = [int(input()) for _ in range(p)]
for i in arr:
    t = find(i)
    if t == 0: break
    union(t,t-1)
    ans += 1
print(ans)