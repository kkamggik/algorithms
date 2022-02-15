from collections import deque
import sys
input = sys.stdin.readline
dirc = [[1,0],[0,1],[-1,0],[0,-1]]
def bfs(x,y,flag):
    visited = deque()
    queue = deque()
    queue.append([x,y])
    visit[y][x] = 1
    people, cnt = 0,0
    while queue:
        x,y = queue.popleft()
        people += arr[y][x]
        cnt += 1
        visited.append([x,y])
        for d in dirc:
            nx,ny = x+d[0],y+d[1]
            if 0<=nx<n and 0<=ny<n and s<=abs(arr[ny][nx]-arr[y][x])<=e and visit[ny][nx]==0:
                queue.append([nx,ny])
                visit[ny][nx] = 1
    if cnt == 1: return True
    rem = people // cnt
    while visited:
        x,y = visited.popleft()
        arr[y][x] = rem
    return False

n,s,e = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
answer = 0
while True:
    visit = [[0]*n for _ in range(n)]
    flag = True
    for i in range(n):
        for j in range(n):
            if visit[i][j]==0:
                if bfs(j,i, flag)==False:
                    flag = False
    if flag == True: break
    answer += 1
print(answer)