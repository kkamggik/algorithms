import sys
input = sys.stdin.readline
answer = 2e9
def travel(start,v,s,cnt):
    global visited, answer
    if cnt == n:
        if arr[v][start] != 0:
            answer = min(answer,s+arr[v][start])
        return
    for nxt in range(n):
        if nxt!=v and arr[v][nxt]!=0 and visited[nxt]==0:
            visited[nxt] = 1
            travel(start,nxt,s+arr[v][nxt],cnt+1)
            visited[nxt] = 0
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [0]*n
for i in range(n):
    visited[i] = 1
    travel(i,i,0,1)
    visited[i] = 0
print(answer)