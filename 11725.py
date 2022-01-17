import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline
def dfs(v,root):
    visited[v] = root
    for adj in arr[v]:
        if visited[adj]==0:
            dfs(adj,v)
n = int(input())
arr = [[] for _ in range(n+1)]
for _ in range(n-1):
    a,b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)
visited = [0]*(n+1)
dfs(1,1)
for v in visited[2:]: print(v)
