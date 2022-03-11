import sys
input = sys.stdin.readline
def find(x):
    if parent[x]==x: return x
    parent[x] = find(parent[x])
    return parent[x]
def union(a,b):
    x = find(a)
    y = find(b)
    if x > y: parent[x] = y
    else: parent[y] = x
n,m = map(int, input().split())
arr = []
for _ in range(m):
    a,b,c = map(int, input().split())
    arr.append([c,a,b])
arr.sort()
parent = [i for i in range(n+1)]
answer = 0 
for c,a,b in arr:
    if find(a)!=find(b):
        union(a,b)
        answer += c
print(answer)
