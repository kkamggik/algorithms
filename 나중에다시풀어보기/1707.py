import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
def bipartite(v, val):
    visited[v] = val
    for nxt in arr[v]:
        if visited[nxt]==0:
            bipartite(nxt, -val)
        elif visited[nxt]==val:
            global answer
            answer = False
            return
tests = int(input())
for t in range(tests):
    n,m = map(int, input().split())
    visited = [0]*(n+1)
    arr = [[] for _ in range(n+1)]
    for _ in range(m):
        a,b = map(int, input().split())
        arr[a].append(b)
        arr[b].append(a)
    answer = True
    for i in range(1,n+1):
        if visited[i]==0 and answer==True:
            bipartite(i,1)
    if answer==True: print('YES')
    else: print('NO')