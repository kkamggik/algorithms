import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
def dfs(idx,parent):
    parents[idx] = parent
    for nxt in arr[idx]:
        if parents[nxt]==-1:
            dfs(nxt, idx)
n = int(input())
arr = [[] for _ in range(n+1)]
for _ in range(n-1):
    a,b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)
parents = [-1]*(n+1)
dfs(1,1)
for i in range(2,n+1): print(parents[i])