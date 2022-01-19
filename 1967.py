import sys
from collections import deque 
input = sys.stdin.readline
def bfs(idx,mode):
    queue = deque()
    queue.append([idx,0])
    visited = [-1]*(n+1)
    visited[idx] = 0
    while queue:
        x,d = queue.popleft()
        for dist,adj in arr[x]:
            if visited[adj]==-1:
                visited[adj] = d+dist
                queue.append([adj,visited[adj]])
    if mode == 1:
        mx = max(visited)
        return visited.index(mx)
    else:
        return max(visited)
n = int(input())
arr = [[] for _ in range(n+1)]
for _ in range(n-1):
    a,b,c = map(int, input().split())
    arr[a].append([c,b])
    arr[b].append([c,a])
mdist = bfs(1,1)
print(bfs(mdist,2))
