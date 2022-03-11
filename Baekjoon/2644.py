import sys
input = sys.stdin.readline
def dfs(idx,cnt):
    if idx == y:
        global answer
        answer = min(answer, cnt)
        return
    for adj in arr[idx]:
        if visited[adj]==0:
            visited[adj] = 1
            dfs(adj,cnt+1)
            visited[adj] = 0
n = int(input())
x,y = map(int, input().split())
m = int(input())
arr = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)
answer = 1e9
visited = [0]*(n+1)
visited[x] = 1
dfs(x,0)
if answer == 1e9: answer = -1
print(answer)