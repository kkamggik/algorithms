class Solution(object):
    def bfs(self, x, y, board):
        n,m = len(board), len(board[0])
        global visited
        queue = deque()
        visited[y][x] = 1
        queue.append([x,y])
        dirc = [[1,0],[-1,0],[0,1],[0,-1]]
        flip = deque()
        flip.append([x,y])
        if x==0 or y==0 or x==m-1 or y==n-1: flag = False
        else: flag = True
        while queue:
            x,y = queue.popleft()
            for d in dirc:
                nx,ny = x+d[0], y+d[1]
                if 0<=nx<m and 0<=ny<n and visited[ny][nx]==0 and board[ny][nx]=='O':
                    if nx==0 or ny==0 or nx==m-1 or ny==n-1: flag = False
                    queue.append([nx,ny])
                    flip.append([nx,ny])
                    visited[ny][nx] = 1
        if flag == True:
            while flip:
                x,y = flip.popleft()
                board[y][x] = 'X'
            
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        n,m = len(board), len(board[0])
        global visited
        visited = [[0]*m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if board[i][j] == 'O' and visited[i][j]==0:
                    self.bfs(j,i,board)