from collections import deque
def bfs(x, arr):
    visited = [False]*(n+1)
    cnt = 0
    queue = deque()
    queue.append(x)
    visited[x] = True
    while queue:
        q = queue.popleft()
        for t in arr[q]:
            if not visited[t]:
                visited[t] = True
                queue.append(t)
                cnt += 1
    return cnt
n,m,x = map(int, input().split())
arr = [[] for _ in range(n+1)]
rev = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int, input().split())
    arr[a].append(b)
    rev[b].append(a)
print(1+bfs(x,rev), n-bfs(x,arr))