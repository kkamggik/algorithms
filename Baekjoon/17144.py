from collections import deque
from copy import deepcopy
import sys
input = sys.stdin.readline
dirc = [[0,1],[0,-1],[1,0],[-1,0]]
n,m,t = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
air = []
for _ in range(t):
    # 새로운 배열만들어서 미세먼지 확산 계산해야뎅
    new = [[0]*m for _ in range(n)]
    # 현재 먼지있는 위치 다 큐에 집어넣기
    dust = deque()
    for i in range(n):
        for j in range(m):
            if arr[i][j] == -1:
                new[i][j] = -1
                air.append([j,i])
            if arr[i][j] > 0: dust.append([j,i])
    # 미세먼지 확산되는중..!!
    while dust:
        x,y = dust.popleft()
        spread = arr[y][x]//5
        cnt = 0
        for d in dirc:
            nx,ny = x+d[0],y+d[1]
            # 배열 밖으로 나가거나 공기청정기 있는 방향으로는 확산이 일어나지않아용
            if 0<=nx<m and 0<=ny<n and new[ny][nx]!=-1:
                new[ny][nx] += spread
                cnt += 1
        new[y][x] += arr[y][x]-(spread*cnt)
    # 공기청정기 작동...!!
    # 우선 윗방향부터 처리하자
    sx,sy = air[0][0], air[0][1]
    nx,ny = sx+1, sy
    d = 2
    val = new[ny][nx]
    new[ny][nx] = 0
    while True:
        if nx == m-1 and d==2: d=1
        elif ny == 0 and d==1: d=3
        elif nx == 0 and d==3: d=0
        nx,ny = nx+dirc[d][0], ny+dirc[d][1]
        if nx==sx and ny==sy: break
        temp = new[ny][nx]
        new[ny][nx] = val
        val = temp
    # 그 다음엔 밑방향
    sx,sy = air[1][0], air[1][1]
    nx,ny = sx+1, sy
    d = 2
    val = new[ny][nx]
    new[ny][nx] = 0
    while True:
        if nx == m-1 and d==2: d=0
        elif ny == n-1 and d==0: d=3
        elif nx == 0 and d==3: d=1
        nx,ny = nx+dirc[d][0], ny+dirc[d][1]
        if nx==sx and ny==sy: break
        temp = new[ny][nx]
        new[ny][nx] = val
        val = temp
    arr = deepcopy(new)
answer = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] > 0: answer += arr[i][j]
print(answer)