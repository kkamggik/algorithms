class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        n,m = len(board), len(board[0])
        dirc = [[1,0],[-1,0],[0,1],[0,-1],[1,1],[-1,1],[1,-1],[-1,-1]]
        for i in range(n):
            for j in range(m):
                live = board[i][j]
                d,l = 0,0
                for di in dirc:
                    x = j+di[0]
                    y = i+di[1]
                    if 0<=x<m and 0<=y<n:
                        if board[y][x]==1 or board[y][x]==2: l += 1
                        else: d += 1
                if live and l<2: board[i][j] = 2
                elif live and l>3: board[i][j] = 2
                elif not live and l==3: board[i][j] = -2
        for i in range(n):
            for j in range(m):
                if board[i][j]==-2: board[i][j]=1
                elif board[i][j]==2: board[i][j]=0
