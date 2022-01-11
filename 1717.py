import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)  
def find(x):
    if parents[x]==x: return x
    parents[x] = find(parents[x])
    return parents[x]
def union(a,b):
    a = find(a)
    b = find(b)
    if a > b:
        parents[a] = b
    else:
        parents[b] = a
n,m = map(int, input().split())
parents = [i for i in range(n+1)]
for _ in range(m):
    c,a,b = map(int, input().split())
    if c == 0: union(a,b)
    else:
        if find(a)==find(b): print('YES')
        else: print('NO')