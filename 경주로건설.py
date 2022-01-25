from collections import deque
dirc = [[1,0],[-1,0],[0,1],[0,-1]]
def solution(board):
    answer = 2e9
    n = len(board)
    visited = [[[1e9 for i in range(n)] for j in range(n)] for k in range(4)]
    queue = deque()
    for i in range(4):
        visited[i][0][0] = 0
        queue.append([0,0,i,0])
    while queue:
        x,y,d,c = queue.popleft()
        for i in range(4):
            dx = dirc[i]
            nx,ny = x+dx[0], y+dx[1]
            if 0<=nx<n and 0<=ny<n and board[ny][nx]==0:
                if d!=i: ncost = c+600
                else: ncost = c+100
                if visited[i][ny][nx] > ncost:
                    visited[i][ny][nx] = ncost
                    queue.append([nx,ny,i,ncost])
    for i in range(4):
        answer = min(answer, visited[i][n-1][n-1])
    return answer
print(solution([[0, 0, 1, 0], [0, 0, 0, 0], [0, 1, 0, 1], [1, 0, 0, 0]]))