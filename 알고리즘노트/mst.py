def find(x):
    if parent[x]==x: return x
    parent[x] = find(parent[x])
    return parent[x]
def union(a,b):
    x = find(a)
    y = find(b)
    if x < y: parent[y] = x
    else: parent[x] = y
parent = [i for i in range(n+1)]