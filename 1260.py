from collections import deque
def dfs(s, visit):
    visit[s] = 1
    print(s, end=' ')
    for i in range(1,n+1):
        if arr[s][i] == 1 and visit[i]==0:
            dfs(i, visit)
def bfs(s, visit):
    queue = deque()
    queue.append(s)
    visit[s] = 1
    while queue:
        x = queue.popleft()
        print(x, end=' ')
        for i in range(1,n+1):
            if arr[x][i] == 1 and visit[i]==0:
                queue.append(i)
                visit[i] = 1

n,m,s = map(int, input().split())
arr = [[0]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a,b = map(int, input().split())
    arr[a][b] = 1
    arr[b][a] = 1
visit = [0]*(n+1)
dfs(s, visit)
print()
visit = [0]*(n+1)
bfs(s, visit)