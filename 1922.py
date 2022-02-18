import sys
input = sys.stdin.readline
def find(x):
    if parent[x]==x: return x
    parent[x] = find(parent[x])
    return parent[x]
def union(a,b):
    x = find(a)
    y = find(b)
    if x < y: parent[y] = x
    else: parent[x] = y
n = int(input())
m = int(input())
edges = []
for _ in range(m):
    a,b,c = map(int, input().split())
    edges.append([c,a,b])
edges.sort()
parent = [i for i in range(n+1)]
answer = 0
for cost,v1,v2 in edges:
    if find(v1)!=find(v2):
        union(v1,v2)
        answer += cost
print(answer)