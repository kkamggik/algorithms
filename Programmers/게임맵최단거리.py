from collections import deque
dirc = [[1,0],[-1,0],[0,1],[0,-1]]
def bfs(maps):
    n,m = len(maps),len(maps[0])
    visited = [[0]*m for _ in range(n)]
    queue = deque()
    queue.append([0,0,1])
    visited[0][0] = 1
    answer = 1e9
    while queue:
        x,y,cnt = queue.popleft()
        if x==m-1 and y==n-1:
            answer = min(answer,cnt)
            break
        for d in dirc:
            nx,ny = x+d[0],y+d[1]
            if 0<=nx<m and 0<=ny<n and visited[ny][nx]==0 and maps[ny][nx]==1:
                visited[ny][nx] = cnt+1
                queue.append([nx,ny,cnt+1])
    if answer==1e9: return -1
    return answer
def solution(maps):
    answer = bfs(maps)
    return answer
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))