def find(x):
    if parent[x]!=x:
        parent[x] = find(parent[x])
    return parent[x]
def union(x,y):
    a = find(x)
    b = find(y)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
n,m = map(int, input().split())
parent = [i for i in range(n+1)]
edges = []
for _ in range(m):
    a,b,c = map(int, input().split())
    edges.append([c,a,b])
edges.sort()
cost = 0
last = 0
for c,a,b in edges:
    if find(a)!=find(b):
        union(a,b)
        cost += c
        last = c
print(cost - last)