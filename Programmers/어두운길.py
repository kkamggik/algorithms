def find(x):
    if parent[x]!=x:
        parent[x] = find(parent[x])
    return parent[x]
def union(a,b):
    x = find(a)
    y = find(b)
    if x > y:
        parent[x] = y
    else:
        parent[y] = x
n,m = map(int, input().split())
parent = [i for i in range(n+1)]
edges = []
total = 0
for _ in range(m):
    x,y,z = map(int, input().split())
    edges.append([z,x,y])
    total += z
edges.sort()
rst = 0
for edge in edges:
    cost,a,b = edge
    if find(a) != find(b):
        union(a,b)
        rst += cost
print(total-rst)
