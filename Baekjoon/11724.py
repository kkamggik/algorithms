import sys
sys.setrecursionlimit(10000)
def dfs(idx, flag):
    visited[idx] = flag
    for nxt in arr[idx]:
        if visited[nxt] == 0:
            dfs(nxt,flag)
n,m = map(int, input().split())
arr = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)
visited = [0]*(n+1)
flag = 1
for i in range(1,n+1):
    if visited[i] == 0:
        dfs(i,flag)
        flag += 1
print(max(visited))
