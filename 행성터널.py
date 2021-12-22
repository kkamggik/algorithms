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
n = int(input())
parent = [i for i in range(n+1)]
edges = []
x = []
y = []
z = []
for i in range(1,n+1):
    a,b,c = map(int, input().split())
    x.append([a,i])
    y.append([b,i])
    z.append([c,i])
x.sort()
y.sort()
z.sort()
for i in range(n-1):
    edges.append([x[i+1][0]-x[i][0], x[i][1], x[i+1][1]])
    edges.append([y[i+1][0]-y[i][0], y[i][1], y[i+1][1]])
    edges.append([z[i+1][0]-z[i][0], z[i][1], z[i+1][1]])
edges.sort()
rst = 0
for edge in edges:
    cost,a,b = edge
    if find(a)!=find(b):
        union(a,b)
        rst += cost
print(rst)